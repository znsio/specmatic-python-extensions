from time import sleep
from specmatic.servers.wsgi_server_thread import WSGIServerThread
from specmatic.utils import find_available_port


class WSGIServer:
    server: WSGIServerThread = None

    def __init__(self, app, host: str = '127.0.0.1', port: int = 0):
        self.app = app
        self.host = host
        self.port = find_available_port() if port == 0 else port
        self.daemon = True

    def start(self):
        self.server = WSGIServerThread(self.app, self.host, self.port)
        self.server.start()
        sleep(2)

    def stop(self):
        self.server.shutdown()
