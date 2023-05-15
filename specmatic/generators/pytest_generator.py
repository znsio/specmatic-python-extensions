import pytest

from specmatic.generators.test_generator_base import TestGeneratorBase


class PyTestGenerator(TestGeneratorBase):

    def __init__(self, test_class, junit_report_path):
        self.test_class = test_class
        self.junit_report_path = junit_report_path

    def generate(self):
        self.generate_tests(self.junit_report_path, self.test_class,  PyTestGenerator._generate_passing_test,
                            PyTestGenerator._generate_failing_test)

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
