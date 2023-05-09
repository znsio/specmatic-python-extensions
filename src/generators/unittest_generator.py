import xml.etree.ElementTree as ET


class UnitTestGenerator:

    def __init__(self, test_class, junit_report_path):
        self.test_class = test_class
        self.junit_report_path = junit_report_path

    def _gen_passing_test(self):
        def test(self):
            self.assertTrue(1 == 1)

        return test

    def _gen_failing_test(self, error):
        def test(self):
            self.fail(error)

        return test

    def generate(self):
        root = ET.parse(self.junit_report_path).getroot()
        for testcase in root.iter('testcase'):
            scenario = testcase.find('system-out').text.split('display-name:  ')[1]
            test_name = "test_" + scenario
            failure = testcase.find('failure')
            if failure is None:
                setattr(self.test_class, test_name, self._gen_passing_test())
            else:
                setattr(self.test_class, test_name, self._gen_failing_test(failure.get('message') + failure.text))
