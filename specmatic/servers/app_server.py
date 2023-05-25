import subprocess
import threading
import traceback
from queue import Queue
from specmatic.utils import find_available_port


class AppServer:

    def __init__(self, app_module: str, host: str = '127.0.0.1', port: int = 0):
        self.__process = None
        self.app_module = app_module
        self.host = host
        self.port = find_available_port() if port == 0 else port
        self.__app_server_started_message = f'Uvicorn running on http://{self.host}:{self.port} (Press CTRL+C to quit)'
        self.__app_started_event = threading.Event()
        self.__error_queue = Queue()

    def start(self):
        self.__start_app_in_subprocess()
        self.__start_reading_app_output()
        self.__wait_till_app_has_started()

    def __start_app_in_subprocess(self):
        cmd = ["uvicorn", self.app_module, "--host=" + self.host, "--port=" + str(self.port)]
        self.__process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def __wait_till_app_has_started(self):
        self.__app_started_event.wait()
        if not self.__error_queue.empty():
            error = self.__error_queue.get()
            raise Exception(f"An exception occurred while reading the app process output: {error}")

    def __start_reading_app_output(self):
        stdout_reader = threading.Thread(target=self.__read_process_output, daemon=True)
        stdout_reader.start()

    def __read_process_output(self):
        try:
            for line in iter(self.__process.stdout.readline, ''):
                if line:
                    line = line.decode().rstrip()
                    print(line)
                    if self.__app_server_started_message in line:
                        self.__app_started_event.set()
        except Exception:
            tb = traceback.format_exc()
            self.__error_queue.put(tb)
            self.__app_started_event.set()

    def stop(self):
        print("Stopping app server...")
        self.__process.terminate()
