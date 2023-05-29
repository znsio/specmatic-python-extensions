from specmatic.core.specmatic import Specmatic


def specmatic_stub(host: str = '127.0.0.1', port: int = 0, project_root: str = '', expectations=None,
                   contract_files=None,
                   specmatic_json_file: str = ''):
    def decorator(cls):
        try:
            cls.stub = Specmatic.start_stub(host, port, project_root, contract_files, specmatic_json_file)
            cls.stub.set_expectations(expectations)
        except Exception as e:
            if hasattr(cls, 'stub'):
                cls.stub.stop()
            if hasattr(cls, 'app'):
                cls.app.stop()
            print(f"Error: {e}")
            raise e
        return cls

    return decorator


def specmatic_contract_test(host: str = '127.0.0,1', port: int = 0, project_root: str = '', contract_files=None,
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

            Specmatic.test(cls, test_host, test_port, project_root, contract_files, specmatic_json_file)
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


def start_wsgi_app(app, host: str = '127.0.0.1', port: int = 0):
    def decorator(cls):
        try:
            cls.app = Specmatic.start_wsgi_app(app, host, port)
            return cls
        except Exception as e:
            if hasattr(cls, 'stub'):
                cls.stub.stop()
            if hasattr(cls, 'app'):
                cls.app.stop()
            print(f"Error: {e}")
            raise e

    return decorator


def start_asgi_app(app_module: str, host: str = '127.0.0.1', port: int = 0):
    def decorator(cls):
        try:
            cls.app = Specmatic.start_asgi_app(app_module, host, port)
            return cls
        except Exception as e:
            if hasattr(cls, 'stub'):
                cls.stub.stop()
            if hasattr(cls, 'app'):
                cls.app.stop()
            print(f"Error: {e}")
            raise e

    return decorator
