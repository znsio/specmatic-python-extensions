import re
import xml.etree.ElementTree as ET
from typing import Callable, Type

class TestGeneratorBase:
    pattern = re.compile(r"[\s\S]*dynamic-test:#(\d+)[\s\S]*Scenario: (.*)\n[\s\S]*")
    @staticmethod
    def generate_tests(junit_report_path: str, test_class: Type, passing_test_fn: Callable, failing_test_fn: Callable) -> None:
        try:
            root = ET.parse(junit_report_path).getroot()
            for testcase in root.iter('testcase'):
                test_case_info = re.match(TestGeneratorBase.pattern, testcase.find('system-out').text) # type: ignore
                if test_case_info is None:
                    raise ValueError("Invalid test case information")
                unique_id, scenario = test_case_info.groups()
                test_name = f"test_scenario_{unique_id} {scenario}"
                failure_message = testcase.findtext('failure')
                if failure_message is None:
                    setattr(test_class, test_name, passing_test_fn())
                else:
                    setattr(test_class, test_name, failing_test_fn(failure_message))
        except ET.ParseError as e:
            raise ValueError("Invalid XML file") from e