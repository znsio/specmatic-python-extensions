import socket
import threading

from specmatic.server.wsgi_server_thread import WSGIServerThread


class WSGIServer:
    server: WSGIServerThread = None

    def __init__(self, app, host: str = '127.0.0.1', port: int = 0):
        self.app = app
        self.host = host
        self.port = self.__find_available_port() if port == 0 else port

    def __find_available_port(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 0))
        port = sock.getsockname()[1]
        sock.close()
        return port

    def start(self):
        self.server = WSGIServerThread(self.app, self.host, self.port)
        self.server.start()
        self.server.wait_for_start()

    def stop(self):
        self.server.shutdown()
