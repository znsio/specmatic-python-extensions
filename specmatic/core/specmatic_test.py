import os
import shutil
import subprocess

from specmatic.utils import get_junit_report_dir_path


class SpecmaticTest:
    def __init__(self, project_root: str, host: str = "127.0.0.1", port: int = 5000, contract_file_path: str = '',
                 specmatic_json_file_path: str = ''):
        self.project_root = project_root
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
            "test"
        ]
        if self.specmatic_json_file_path != '':
            cmd.append("--config=" + self.specmatic_json_file_path)
        else:
            if self.contract_file_path != '':
                cmd.append(self.contract_file_path)
            else:
                cmd.append("--config=" + self.project_root + "/specmatic.json")

        cmd += [
            "--junitReportDir=" + get_junit_report_dir_path(),
            '--host=' + self.host,
            "--port=" + str(self.port)
        ]

        print(f"\n Running specmatic tests for api at {self.host}:{self.port}")
        subprocess.run(cmd)

    def run(self):
        self._delete_existing_report_if_exists()
        self._execute_specmatic()
