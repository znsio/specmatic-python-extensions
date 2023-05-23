import json
import os
import subprocess
import threading
import traceback
from queue import Queue

import requests


class SpecmaticStub:

    def __init__(self, host: str, port: int, specmatic_json_file_path: str, contract_file_path: str):
        self.__stub_started_event = None
        self.__process = None
        self.host = host
        self.port = port
        self.specmatic_json_file_path = specmatic_json_file_path
        self.contract_file_path = contract_file_path
        self.__expectation_api = f'http://{self.host}:{self.port}/_specmatic/expectations'
        self.__stub_running_success_message = f'Stub server is running on http://{self.host}:{self.port}'
        self.__error_queue = Queue()

    def start(self):
        try:
            self.__stub_started_event = threading.Event()
            self.__start_specmatic_stub_in_subprocess()
            self.__start_reading_stub_output()
            self.__wait_till_stub_has_started()
        except Exception as e:
            self.stop()
            print(f"Error: {e}")
            raise e

    def stop(self):
        print(f"\n Shutting down specmatic stub server on {self.host}:{self.port}, please wait ...")
        self.__process.kill()

    def set_expectations(self, file_paths: list[str]):
        if file_paths is None:
            file_paths = []
        try:
            for file_path in file_paths:
                with open(file_path, 'r') as file:
                    json_string = json.load(file)
                    headers = {
                        "Content-Type": "application/json"
                    }
                    response = requests.post(self.__expectation_api, json=json_string, headers=headers)
                    if response.status_code != 200:
                        self.stop()
                        raise Exception(f"{response.content} received for expectation json file: {json_string}")

        except Exception as e:
            self.stop()
            print(f"Error: {e}")
            raise e

    def __start_specmatic_stub_in_subprocess(self):
        stub_command = self.__create_stub_process_command()
        print(f"\n Starting specmatic stub server on {self.host}:{self.port}")
        self.__process = subprocess.Popen(stub_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def __start_reading_stub_output(self):
        stdout_reader = threading.Thread(target=self.__read_process_output, daemon=True)
        stdout_reader.start()

    def __wait_till_stub_has_started(self):
        self.__stub_started_event.wait()
        if not self.__error_queue.empty():
            error = self.__error_queue.get()
            raise Exception(f"An exception occurred while reading the stub process output: {error}")

    def __read_process_output(self):
        def signal_event_if_stub_has_started(line):
            if self.__stub_running_success_message in line:
                self.__stub_started_event.set()

        def read_and_print_output_line_by_line():
            for line in iter(self.__process.stdout.readline, ''):
                if line:
                    line = line.decode().rstrip()
                    print(line)
                    signal_event_if_stub_has_started(line)

        try:
            read_and_print_output_line_by_line()
        except Exception:
            tb = traceback.format_exc()
            self.__error_queue.put(tb)
            self.__stub_started_event.set()

    def __create_stub_process_command(self):
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
