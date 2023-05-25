import threading
from time import sleep

from specmatic.servers.asgi_server_thread import ASGIServerThread
from specmatic.utils import find_available_port


class ASGIServer:
    server: ASGIServerThread = None

    def __init__(self, app, host: str = '127.0.0.1', port: int = 0):
        self.app_server_thread = None
        self.app = app
        self.host = host
        self.port = find_available_port() if port == 0 else port
        self.__app_server_started_message = f'Uvicorn running on http://{self.host}:{self.port} (Press CTRL+C to quit)'
        self.__app_server_started_event = threading.Event()

    def start(self):
        self.app_server_thread = ASGIServerThread(self.app, self.host, self.port)
        self.app_server_thread.start()
        sleep(2)

    def stop(self):
        self.app_server_thread.shutdown()
