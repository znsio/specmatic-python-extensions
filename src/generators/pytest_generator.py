import xml.etree.ElementTree as ET
import pytest


class PyTestGenerator:

    def __init__(self, test_class, junit_report_path):
        self.test_class = test_class
        self.junit_report_path = junit_report_path

    def generate(self):
        root = ET.parse(self.junit_report_path).getroot()
        for testcase in root.iter('testcase'):
            scenario = testcase.find('system-out').text.split('display-name:  ')[1]
            test_name = "test_" + scenario
            failure = testcase.find('failure')
            if failure is None:
                setattr(self.test_class, test_name, self.generate_passing_test())
            else:
                setattr(self.test_class, test_name, self.generate_failing_test(failure.get('message') + failure.text))

    def generate_passing_test(self):
        def test(self):
            assert 1 == 1

        return test

    def generate_failing_test(self, error):
        def test(self):
            pytest.fail(error)

        return test
