from specmatic.generators.test_generator_base import TestGeneratorBase


class UnitTestGenerator(TestGeneratorBase):

    def __init__(self, test_class, junit_report_path):
        self.test_class = test_class
        self.junit_report_path = junit_report_path

    @staticmethod
    def _gen_passing_test():
        def test(self):
            self.assertTrue(1 == 1)

        return test

    @staticmethod
    def _gen_failing_test(error):
        def test(self):
            self.fail(error)

        return test

    def generate(self):
        self.generate_tests(self.junit_report_path, self.test_class, UnitTestGenerator._gen_passing_test,
                            UnitTestGenerator._gen_failing_test)
