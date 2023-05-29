from specmatic.core.specmatic_stub import SpecmaticStub
from specmatic.core.specmatic_test import SpecmaticTest
from specmatic.generators.pytest_generator import PyTestGenerator
from specmatic.servers.app_server import AppServer
from specmatic.servers.wsgi_server import WSGIServer
from specmatic.utils import get_junit_report_file_path


class Specmatic:

    @classmethod
    def start_stub(cls, host: str = '127.0.0.1', port: int = 0, project_root: str = '', contract_file_path: str = '',
                   specmatic_json_file_path: str = '',
                   ):
        stub = None
        try:
            stub = SpecmaticStub(host, port, project_root, contract_file_path, specmatic_json_file_path)
            return stub
        except Exception as e:
            if stub is not None:
                stub.stop()
            print(f"Error: {e}")
            raise e

    @classmethod
    def test(cls, test_class, host: str = '127.0.0.1', port: int = 0, project_root: str = '',
             contract_file_path: str = '',
             specmatic_json_file_path: str = ''
             ):
        try:
            SpecmaticTest(host, port, project_root, contract_file_path, specmatic_json_file_path).run()
            PyTestGenerator(test_class, get_junit_report_file_path()).generate()
        except Exception as e:
            print(f"Error: {e}")
            raise e

    @classmethod
    def start_wsgi_app(cls, app, host: str = '127.0.0.1', port: int = 0):
        app_server = None
        try:
            app_server = WSGIServer(app, host, port)
            app_server.start()
            return app_server
        except Exception as e:
            if app_server is not None:
                app_server.stop()
            print(f"Error: {e}")
            raise e

    @classmethod
    def start_asgi_app(cls, app_module, host: str = '127.0.0.1', port: int = 0):
        app_server = None
        try:
            app_server = AppServer(app_module, host, port)
            app_server.start()
            return app_server
        except Exception as e:
            if app_server is not None:
                app_server.stop()
            print(f"Error: {e}")
            raise e

    @classmethod
    def test_wsgi_app(cls, app, test_class, project_root: str = '', app_contract_file: str = '',
                      stub_contract_file: str = '',
                      expectation_files: [] = None, app_host: str = '127.0.0.1', app_port: int = 0,
                      stub_host: str = '127.0.0.1', stub_port: int = 0, app_config_update_func=None):

        stub = None
        app_server = None

        try:
            stub = Specmatic.start_stub(stub_host, stub_port, project_root, contract_file_path=stub_contract_file)
            stub.set_expectations(expectation_files)
            if app_config_update_func is not None:
                app_config_update_func(app, stub)
            app_server = Specmatic.start_wsgi_app(app, app_host, app_port)
            Specmatic.test(test_class, app_server.host, app_server.port, project_root,
                           contract_file_path=app_contract_file)
        except Exception as e:
            print(f"Error: {e}")
            raise e
        finally:
            if app_server is not None:
                app_server.stop()
            if stub is not None:
                stub.stop()

    @classmethod
    def test_asgi_app(cls, app_module, test_class, project_root: str = '', app_contract_file: str = '',
                      stub_contract_file: str = '',
                      expectation_files: [] = None, app_host: str = '127.0.0.1', app_port: int = 0,
                      stub_host: str = '127.0.0.1', stub_port: int = 0):

        stub = None
        app_server = None

        try:
            stub = Specmatic.start_stub(stub_host, stub_port, project_root, contract_file_path=stub_contract_file)
            stub.set_expectations(expectation_files)
            app_server = Specmatic.start_asgi_app(app_module, app_host, app_port)
            Specmatic.test(test_class, app_server.host, app_server.port, project_root,
                           contract_file_path=app_contract_file)
        except Exception as e:
            print(f"Error: {e}")
            raise e
        finally:
            if app_server is not None:
                app_server.stop()
            if stub is not None:
                stub.stop()
