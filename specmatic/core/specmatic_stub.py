import json
import os
import subprocess
import threading
import traceback
from queue import Queue

import requests


class SpecmaticStub:

    def __init__(self, host: str, port: int, specmatic_json_file_path: str, contract_file_path: str):
        self.stub_started_event = None
        self.process = None
        self.host = host
        self.port = port
        self.specmatic_json_file_path = specmatic_json_file_path
        self.contract_file_path = contract_file_path
        self.expectation_api = f'http://{self.host}:{self.port}/_specmatic/expectations'
        self.stub_running_success_message = f'Stub server is running on http://{self.host}:{self.port}'
        self.error_queue = Queue()

    def start(self):
        self.stub_started_event = threading.Event()
        stub_command = self._create_stub_process_command()
        print(f"\n Starting specmatic stub server on {self.host}:{self.port}")
        self.process = subprocess.Popen(stub_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout_reader = threading.Thread(target=self.read_process_output, daemon=True)
        stdout_reader.start()

    def read_process_output(self):
        def signal_event_if_stub_has_started(line):
            if self.stub_running_success_message in line:
                self.stub_started_event.set()

        def read_and_print_output_line_by_line():
            for line in iter(self.process.stdout.readline, ''):
                if line:
                    line = line.decode().rstrip()
                    print(line)
                    signal_event_if_stub_has_started(line)

        try:
            read_and_print_output_line_by_line()
        except Exception:
            tb = traceback.format_exc()
            self.error_queue.put(tb)
            self.stub_started_event.set()

    def stop(self):
        print(f"\n Shutting down specmatic stub server on {self.host}:{self.port}, please wait ...")
        self.process.kill()

    def set_expectations(self, file_paths: list[str]):
        self.stub_started_event.wait()
        if not self.error_queue.empty():
            error = self.error_queue.get()
            raise Exception(f"An exception occurred while reading the stub process output: {error}")

        for file_path in file_paths:
            with open(file_path, 'r') as file:
                json_string = json.load(file)
                headers = {
                    "Content-Type": "application/json"
                }
                response = requests.post(self.expectation_api, json=json_string, headers=headers)
                if response.status_code != 200:
                    self.stop()
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
