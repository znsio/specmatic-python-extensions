import json
import os
import signal
import subprocess
import requests
from time import sleep


class SpecmaticStub:

    def __init__(self, host: str, port: int, specmatic_json_file_path: str, contract_file_path: str):
        self.process = None
        self.host = host
        self.port = port
        self.specmatic_json_file_path = specmatic_json_file_path
        self.contract_file_path = contract_file_path
        self.expectation_api = f'http://{self.host}:{self.port}/_specmatic/expectations'

    def start(self):
        stub_command = self._create_stub_process_command()
        self.process = subprocess.Popen(stub_command)
        print(f"\n Starting specmatic stub server on {self.host}:{self.port}")

    def stop(self):
        print(f"\n Shutting down specmatic stub server on {self.host}:{self.port}, please wait ...")
        sleep(10)
        self._quick_stop()

    def _quick_stop(self):
        self.process.kill()


    def set_expectations(self, file_paths: list[str]):
        sleep(5)
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                json_string = json.load(file)
                headers = {
                    "Content-Type": "application/json"
                }
                response = requests.post(self.expectation_api, json=json_string, headers=headers)
                if response.status_code != 200:
                    self._quick_stop()
                    raise Exception(f"{response.content} received for expectation json file: {json_string}")

    def _create_stub_process_command(self):
        jar_path = os.path.dirname(os.path.realpath(__file__)) + "/specmatic.jar"
        cmd = [
            "java",
            "-jar",
            jar_path,
            "stub"
        ]
        if self.specmatic_json_file_path != '':
            cmd.append("--config=" + self.specmatic_json_file_path)
        else:
            if self.contract_file_path != '':
                cmd.append(self.contract_file_path)
        cmd += [
            '--host=' + self.host,
            "--port=" + str(self.port)
        ]
        return cmd
