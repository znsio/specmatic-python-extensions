import os

import xml.etree.ElementTree as ET
import pytest

from src.specmatic_runner import SpecmaticRunner


class SpecmaticServer:
    test_server_host = "127.0.0.1"
    test_server_port = 5000
    contract_file_path = ''
    specmatic_json_file_path = ''

    def _gen_passing_test(self):
        def test(self):
            self.assertTrue(1 == 1)

        return test

    def _gen_failing_test(self, error):
        def test(self):
            self.fail(error)

        return test

    def _generate_tests(self, test_class):
        junit_report_path = "./junit_report/TEST-junit-jupiter.xml"
        root = ET.parse(junit_report_path).getroot()
        for testcase in root.iter('testcase'):
            scenario = testcase.find('system-out').text.split('display-name:  ')[1]
            test_name = "test_" + scenario
            failure = testcase.find('failure')
            if failure is None:
                setattr(test_class, test_name, self._gen_passing_test())
            else:
                setattr(test_class, test_name, self._gen_failing_test(failure.get('message') + failure.text))

    def _gen_passing_pytest(self):
        def test(self):
            assert 1 == 1

        return test

    def _gen_failing_pytest(self, error):
        def test(self):
            pytest.fail(error)

        return test

    def _generate_pytests(self, test_class):
        junit_report_path = "./junit_report/TEST-junit-jupiter.xml"
        root = ET.parse(junit_report_path).getroot()
        for testcase in root.iter('testcase'):
            scenario = testcase.find('system-out').text.split('display-name:  ')[1]
            test_name = "test_" + scenario
            failure = testcase.find('failure')
            if failure is None:
                setattr(test_class, test_name, self._gen_passing_pytest())
            else:
                setattr(test_class, test_name, self._gen_failing_pytest(failure.get('message') + failure.text))

    def with_api_under_test_at(self, test_server_host: str, test_server_port: int):
        self.test_server_host = test_server_host
        self.test_server_port = test_server_port
        return self

    def with_contract_file(self, contract_file_path: str):
        self.contract_file_path = contract_file_path
        return self

    def with_specmatic_json_at(self, specmatic_json_file_path: str):
        self.specmatic_json_file_path = os.path.abspath(specmatic_json_file_path)
        return self

    def configure_unit_tests(self, test_class):
        SpecmaticRunner(self.test_server_host, self.test_server_port, self.contract_file_path,
                        self.specmatic_json_file_path).run()
        self._generate_tests(test_class)

    def configure_py_tests(self, test_class):
        SpecmaticRunner(self.test_server_host, self.test_server_port, self.contract_file_path,
                        self.specmatic_json_file_path).run()
        self._generate_pytests(test_class)
