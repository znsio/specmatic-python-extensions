import os

from specmatic.server.wsgi_server import WSGIServer
from specmatic.core.specmatic import Specmatic


def specmatic_stub(project_root: str, host: str = '127.0.0.1', port: int = 0, expectations=None, contract_file='',
                   specmatic_json_file: str = ''):
    def decorator(cls):
        try:
            stub = Specmatic.start_stub(project_root, host, port, specmatic_json_file, contract_file)
            cls.stub = stub
            stub.set_expectations(expectations)
        except Exception as e:
            if hasattr(cls, 'stub'):
                cls.stub.stop()
            if hasattr(cls, 'app'):
                cls.app.stop()
            print(f"Error: {e}")
            raise e
        return cls

    return decorator


def specmatic_contract_test(project_root: str, host: str = '127.0.0,1', port: int = 0, contract_file='',
                            specmatic_json_file: str = ''):
    def decorator(cls):
        try:
            test_host = host
            test_port = port
            if test_port == 0:
                if hasattr(cls, 'app'):
                    app = cls.app
                    test_host = app.host
                    test_port = app.port

            Specmatic.test(project_root, cls, test_host, test_port, specmatic_json_file, contract_file)
            return cls
        except Exception as e:
            if hasattr(cls, 'stub'):
                cls.stub.stop()
            if hasattr(cls, 'app'):
                cls.app.stop()
            print(f"Error: {e}")
            raise e
        finally:
            if hasattr(cls, 'stub'):
                cls.stub.stop()
            if hasattr(cls, 'app'):
                cls.app.stop()

    return decorator


def start_app(app, host: str = '127.0.0.1', port: int = 0):
    def decorator(cls):
        try:
            wsgi_app = WSGIServer(app, host, port)
            wsgi_app.start()
            cls.app = wsgi_app
            return cls
        except Exception as e:
            if hasattr(cls, 'stub'):
                cls.stub.stop()
            if hasattr(cls, 'app'):
                cls.app.stop()
            print(f"Error: {e}")
            raise e

    return decorator
