import os
import pathlib
import subprocess


class SpecmaticRunner:
    def __init__(self, host: str = "127.0.0.1", port: int = 5000, contract_file_path: str = '',
                 specmatic_json_file_path: str = ''):
        self.host = host
        self.port = port
        self.contract_file_path = contract_file_path
        self.specmatic_json_file_path = specmatic_json_file_path

    def run(self):
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
            "--junitReportDir=junit_report",
            '--host=' + self.host,
            "--port=" + str(self.port)
        ]

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        output, error = process.communicate()

        # Print the output
        print(output.decode('utf-8'))
