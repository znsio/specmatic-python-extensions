import unittest

from specmatic.core.specmatic_stub import SpecmaticStub
from specmatic.core.specmatic_test import SpecmaticTest
from specmatic.generators.pytest_generator import PyTestGenerator
from specmatic.generators.unittest_generator import UnitTestGenerator
from specmatic.servers.app_server import AppServer
from specmatic.servers.asgi_app_server import ASGIAppServer
from specmatic.servers.wsgi_app_server import WSGIAppServer
from specmatic.utils import get_junit_report_file_path


class Specmatic:
    def __init__(self):
        self.reset_app_config_func = None
        self.set_app_config_func = None
        self.app_host = '127.0.0.1'
        self.app_port = 0
        self.app_module = ''
        self.app = None
        self.test_args = None
        self.stub_args = None
        self.test_class = None
        self.test_port = None
        self.test_host = None
        self.app_server = None
        self.expectations = None
        self.stub_port = None
        self.stub_host = None
        self.run_stub = False
        self.run_app = False
        self.run_tests = False
        self.project_root = ''
        self.specmatic_json_file_path = ''

    def with_project_root(self, project_root):
        self.project_root = project_root
        return self

    def with_specmatic_json_file_path(self, specmatic_json_file_path):
        self.specmatic_json_file_path = specmatic_json_file_path
        return self

    def with_stub(self, stub_host: str = '127.0.0.1', stub_port: int = 0, expectations=None, args=None):
        self.stub_host = stub_host
        self.stub_port = stub_port
        self.run_stub = True
        self.expectations = expectations
        self.stub_args = args
        return self

    def app(self, app_server: AppServer):
        self.app_server = app_server
        self.run_app = True
        return self

    def with_app(self, app):
        self.app = app
        self.run_app = True
        return self

    def with_app_module(self, app_module: str):
        self.app_module = app_module
        self.run_app = True
        return self

    def with_app_host(self, host: str):
        self.app_host = host
        return self

    def with_app_port(self, port: int):
        self.app_port = port
        return self

    def with_set_app_config_func(self, set_app_config_func):
        self.set_app_config_func = set_app_config_func
        return self

    def with_reset_app_config_func(self, reset_app_config_func):
        self.reset_app_config_func = reset_app_config_func
        return self

    def test(self, test_class, test_host: str = '127.0.0.1', test_port: int = 0, args=None):
        self.test_class = test_class
        self.test_host = test_host
        self.test_port = test_port
        self.test_args = args
        self.run_tests = True
        return self

    def run(self):
        stub = None
        try:
            if self.run_app:
                if self.app is None and self.app_module == '':
                    raise Exception('Please specify either app or app_module.')
                if self.app is not None and self.app_module != '':
                    raise Exception('Please specify only one of app or app_module, and not both.')
                if self.app is not None:
                    self.app_server = WSGIAppServer(self.app, self.app_host, self.app_port, self.set_app_config_func,
                                                    self.reset_app_config_func)
                else:
                    self.app_server = ASGIAppServer(self.app_module, self.app_host, self.app_port, self.set_app_config_func,
                                                    self.reset_app_config_func)
            if self.run_stub:
                stub = SpecmaticStub(self.stub_host, self.stub_port, self.project_root, self.specmatic_json_file_path,
                                     self.stub_args)
                stub.set_expectations(self.expectations)
                self.app_server.set_app_config(stub.host, stub.port)
            if self.run_tests:
                if self.app_server is not None:
                    self.app_server.start()
                    self.test_host = self.app_server.host
                    self.test_port = self.app_server.port
                SpecmaticTest(self.test_host, self.test_port, self.project_root,
                              self.specmatic_json_file_path, self.test_args).run()
                if issubclass(self.test_class, unittest.TestCase):
                    print("Injecting unittest methods")
                    UnitTestGenerator(self.test_class, get_junit_report_file_path()).generate()
                else:
                    print("Injecting pytest methods")
                    PyTestGenerator(self.test_class, get_junit_report_file_path()).generate()
        except Exception as e:
            print(f"Error: {e}")
            raise e
        finally:
            if self.app_server is not None:
                self.app_server.stop()
                self.app_server.reset_app_config()
            if stub is not None:
                stub.stop()
