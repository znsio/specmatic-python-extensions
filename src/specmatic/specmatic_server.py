from src.generators.pytest_generator import PyTestGenerator
from src.generators.unittest_generator import UnitTestGenerator
from src.specmatic.specmatic_runner import SpecmaticRunner
from src.utils import get_junit_report_file_path


class SpecmaticServer:
    test_server_host = "127.0.0.1"
    test_server_port = 5000
    contract_file_path = ''
    specmatic_json_file_path = ''

    def with_api_under_test_at(self, test_server_host: str, test_server_port: int):
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
        SpecmaticRunner(self.test_server_host, self.test_server_port, self.contract_file_path,
                        self.specmatic_json_file_path).run()
        UnitTestGenerator(test_class, get_junit_report_file_path()).generate()

    def configure_py_tests(self, test_class):
        SpecmaticRunner(self.test_server_host, self.test_server_port, self.contract_file_path,
                        self.specmatic_json_file_path).run()
        PyTestGenerator(test_class, get_junit_report_file_path()).generate()
