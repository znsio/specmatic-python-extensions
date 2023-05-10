import os
import pathlib
import subprocess

from specmatic_python.utils import get_junit_report_file_path, get_junit_report_dir_path
import shutil


class SpecmaticRunner:
    def __init__(self, host: str = "127.0.0.1", port: int = 5000, contract_file_path: str = '',
                 specmatic_json_file_path: str = ''):
        self.host = host
        self.port = port
        self.contract_file_path = contract_file_path
        self.specmatic_json_file_path = specmatic_json_file_path

    def _delete_existing_report_if_exists(self):
        junit_report_dir_path = get_junit_report_dir_path()
        if os.path.exists(junit_report_dir_path):
            shutil.rmtree(junit_report_dir_path)

    def _execute_specmatic(self):
        jar_path = os.path.dirname(os.path.realpath(__file__)) + "/specmatic.jar"
        cmd = [
            "java",
            "-jar",
            jar_path,
            "test",
            "--config=" + self.specmatic_json_file_path
        ]
        if self.contract_file_path != '':
            cmd.append(self.contract_file_path)

        cmd += [
            "--junitReportDir=" + get_junit_report_dir_path(),
            '--host=' + self.host,
            "--port=" + str(self.port)
        ]

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        output, error = process.communicate()

        # Print the output
        print(output.decode('utf-8'))

    def run(self):
        self._delete_existing_report_if_exists()
        self._execute_specmatic()
