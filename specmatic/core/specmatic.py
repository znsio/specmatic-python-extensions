from specmatic.generators.pytest_generator import PyTestGenerator
from specmatic.generators.unittest_generator import UnitTestGenerator
from specmatic.core.specmatic_test import SpecmaticTest
from specmatic.core.specmatic_stub import SpecmaticStub
from specmatic.utils import get_junit_report_file_path


class Specmatic:

    def __init__(self):
        self.stub_server_port = None
        self.stub_server_host = None
        self.test_server_port = None
        self.test_server_host = None
        self.contract_file_path = ''
        self.specmatic_json_file_path = ''

    def test(self, test_server_host: str = "127.0.0.1", test_server_port: int = 5000):
        self.test_server_host = test_server_host
        self.test_server_port = test_server_port
        return self

    def with_contract_file(self, contract_file_path: str):
        self.contract_file_path = contract_file_path
        return self

    def with_specmatic_json_at(self, specmatic_json_file_path: str):
        self.specmatic_json_file_path = specmatic_json_file_path
        return self

    def configure_unit_tests(self, test_class):
        SpecmaticTest(self.test_server_host, self.test_server_port, self.contract_file_path,
                      self.specmatic_json_file_path).run()
        UnitTestGenerator(test_class, get_junit_report_file_path()).generate()

    def configure_py_tests(self, test_class):
        SpecmaticTest(self.test_server_host, self.test_server_port, self.contract_file_path,
                      self.specmatic_json_file_path).run()
        PyTestGenerator(test_class, get_junit_report_file_path()).generate()

    def stub(self, stub_server_host: str = '0.0.0.1',
             stub_server_port: int = 9000):
        self.stub_server_host = stub_server_host
        self.stub_server_port = stub_server_port
        return self

    def build(self):
        return SpecmaticStub(self.stub_server_host, self.stub_server_port, self.specmatic_json_file_path,
                             self.contract_file_path)
