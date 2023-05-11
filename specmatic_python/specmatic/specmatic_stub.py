import os
import subprocess

from specmatic_python.specmatic.specmatic_runner import SpecmaticRunner


class SpecmaticStub:

    def __init__(self, host: str, port: int, contract_file_path: str):
        self.process = None
        self.host = host
        self.port = port
        self.contract_file_path = contract_file_path

    def start(self):
        stub_command = self._create_stub_process_command()
        self.process = subprocess.Popen(stub_command)

    def stop(self):
        self.process.kill()

    def _create_stub_process_command(self):
        jar_path = os.path.dirname(os.path.realpath(__file__)) + "/specmatic.jar"
        cmd = [
            "java",
            "-jar",
            jar_path,
            "stub"
        ]
        if self.contract_file_path != '':
            cmd.append(self.contract_file_path)
        cmd += [
            '--host=' + self.host,
            "--port=" + str(self.port)
        ]
