from specmatic.generators.pytest_generator import PyTestGenerator
from specmatic.generators.unittest_generator import UnitTestGenerator
from specmatic.core.specmatic_test import SpecmaticTest
from specmatic.core.specmatic_stub import SpecmaticStub
from specmatic.utils import get_junit_report_file_path


class Specmatic:

    @classmethod
    def start_stub(cls, project_root: str, host: str = '127.0.0.1', port: int = 0, specmatic_json_file_path: str = '',
                   contract_file_path: str = ''):
        stub = None
        try:
            stub = SpecmaticStub(project_root, host, port, specmatic_json_file_path, contract_file_path)
            return stub
        except Exception as e:
            stub.stop()
            print(f"Error: {e}")
            raise e

    @classmethod
    def test(cls, project_root: str, test_class, host: str, port: int, specmatic_json_file_path: str = '',
             contract_file_path: str = ''):
        SpecmaticTest(project_root, host, port, contract_file_path, specmatic_json_file_path).run()
        PyTestGenerator(test_class, get_junit_report_file_path()).generate()

