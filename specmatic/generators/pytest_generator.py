import pytest

from specmatic.generators.test_generator_base import TestGeneratorBase


class PyTestGenerator(TestGeneratorBase):

    def __init__(self, test_class, junit_report_path):
        self.test_class = test_class
        self.junit_report_path = junit_report_path

    def generate(self):
        contract_tests = self.extract_contract_tests(self.junit_report_path)
        for contract_test in contract_tests:
            if contract_test.passed:
                setattr(self.test_class, contract_test.name, PyTestGenerator._generate_passing_test())
            else:
                setattr(self.test_class, contract_test.name, PyTestGenerator._generate_failing_test(contract_test.error_message))


    @staticmethod
    def _generate_passing_test():
        def test(self):
            assert 1 == 1

        return test

    @staticmethod
    def _generate_failing_test(error):
        def test(self):
            pytest.fail(error)

        return test
