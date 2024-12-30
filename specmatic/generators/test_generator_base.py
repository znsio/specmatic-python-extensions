import re
import xml.etree.ElementTree as ET
from typing import Callable, Type

class TestGeneratorBase:
    pattern = re.compile(r"[\s\S]*dynamic-test:#(\d+)[\s\S]*")
    @staticmethod
    def generate_tests(junit_report_path: str, test_class: Type, passing_test_fn: Callable, failing_test_fn: Callable) -> None:
        test_cases = []
        
        try:
            root = ET.parse(junit_report_path).getroot()
            for testcase in root.iter('testcase'):
                test_case_info = re.match(TestGeneratorBase.pattern, testcase.find('system-out').text) # type: ignore
                if test_case_info is None:
                    raise ValueError("Invalid test case information")
                unique_id = test_case_info.groups()[0]
                test_name  = f"test [{unique_id}] {testcase.get('name')}"
                failure_message = testcase.findtext('failure')
                if failure_message is None:
                    test_cases.append((unique_id, test_name, passing_test_fn()))
                else:
                    test_cases.append((unique_id, test_name, failing_test_fn(failure_message)))
        except ET.ParseError as e:
            raise ValueError("Invalid XML file") from e

        test_cases.sort(key=lambda testcase : int(testcase[0]))
        for (unique_id, test_name, test_fn) in test_cases:
            setattr(test_class, test_name, test_fn)
