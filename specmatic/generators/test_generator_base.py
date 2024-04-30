import xml.etree.ElementTree as ET
from typing import List

from specmatic.generators.contract_test import ContractTest


class TestGeneratorBase:
    @staticmethod
    def extract_contract_tests(junit_report_path) -> List[ContractTest]:
        def extract_test_name(testcase) -> str:
            return "test_" + testcase.get('name').strip()

        def get_error_message(failure) -> str:
            return "" if failure is None else failure.get('message')

        root = ET.parse(junit_report_path).getroot()

        contract_tests = [
            ContractTest(
                name=extract_test_name(testcase),
                passed=failure is None,
                error_message=get_error_message(failure)
            )
            for testcase in root.iter('testcase')
            for failure in [testcase.find('failure')]
        ]
        print("Extracted " + str(len(contract_tests)) + " contract test(s)")
        return contract_tests
