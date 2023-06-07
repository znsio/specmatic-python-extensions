import xml.etree.ElementTree as ET


class TestGeneratorBase:
    @staticmethod
    def generate_tests(junit_report_path, test_class, passing_test_fn, failing_test_fn):
        root = ET.parse(junit_report_path).getroot()
        for testcase in root.iter('testcase'):
            scenario = testcase.find('system-out').text.split('display-name:')[1].strip()
            test_name = "test_" + scenario
            failure = testcase.find('failure')
            if failure is None:
                setattr(test_class, test_name, passing_test_fn())
            else:
                setattr(test_class, test_name, failing_test_fn(failure.get('message') + failure.text))
