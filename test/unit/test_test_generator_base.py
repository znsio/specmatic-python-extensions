from specmatic.generators.test_generator_base import TestGeneratorBase
from specmatic.utils import get_project_root


class TestsForTestGeneratorBase:

    @classmethod
    def setup_class(cls):
        junit_report_file = get_project_root() + '/test/resources/TEST-junit-jupiter.xml'
        cls.contract_tests = TestGeneratorBase.extract_contract_tests(junit_report_file)

    def test_extracts_all_testcases_from_junit_report(self):
        assert len(self.contract_tests) == 5

    def test_correctly_identifies_tests_as_passed_or_failed(self):
        passed_tests = [contract_test for contract_test in self.contract_tests if contract_test.passed is True]
        assert len(passed_tests) == 3

        failed_tests = [contract_test for contract_test in self.contract_tests if contract_test.passed is False]
        assert len(failed_tests) == 2

    def test_extracts_failure_reason_for_failed_tests(self):
        failed_tests = [contract_test for contract_test in self.contract_tests if contract_test.passed is False]
        assert len([failed_test for failed_test in failed_tests if failed_test.error_message == 'server error']) == 2
