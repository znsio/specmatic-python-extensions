from flask import Flask
from specmatic.server.wsgi_server import WSGIServer
from specmatic.core.specmatic import Specmatic


def specmatic_stub(project_root: str, host: str, port: int, expectation_json_files=None, contract_file='', specmatic_json_file: str = ''):
    def decorator(cls):
        try:
            stub = Specmatic.create_stub(project_root, host, port, specmatic_json_file, contract_file)
            stub.start()
            cls.stub = stub
            stub.set_expectations(expectation_json_files)
        except Exception as e:
            if hasattr(cls, 'stub'):
                cls.stub.stop()
            if hasattr(cls, 'app'):
                cls.app.stop()
            print(f"Error: {e}")
            raise e
        return cls

    return decorator


def specmatic_contract_test(project_root: str, host: str, port: int, contract_file='', specmatic_json_file: str = ''):
    def decorator(cls):
        try:
            Specmatic.run_tests(project_root, cls, host, port, specmatic_json_file, contract_file)
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


def start_app(app, host: str, port: int):
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
