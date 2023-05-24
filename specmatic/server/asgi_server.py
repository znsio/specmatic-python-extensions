import socket
import threading
from time import sleep

from specmatic.server.asgi_server_thread import ASGIServerThread


class ASGIServer:
    server: ASGIServerThread = None

    def __init__(self, app, host: str = '127.0.0.1', port: int = 0):
        self.app_server_thread = None
        self.app = app
        self.host = host
        self.port = self.__find_available_port() if port == 0 else port
        self.__app_server_started_message = f'Uvicorn running on http://{self.host}:{self.port} (Press CTRL+C to quit)'
        self.__app_server_started_event = threading.Event()

    def __find_available_port(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 0))
        port = sock.getsockname()[1]
        sock.close()
        return port

    def start(self):
        self.app_server_thread = ASGIServerThread(self.app, self.host, self.port)
        self.app_server_thread.start()
        sleep(2)

    def stop(self):
        self.app_server_thread.shutdown()
