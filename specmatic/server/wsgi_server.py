import threading

from specmatic.server.wsgi_server_thread import WSGIServerThread


class WSGIServer:
    server: WSGIServerThread = None

    def __init__(self, app, host: str, port: int):
        self.app = app
        self.host = host
        self.port = port

    def start(self):
        self.server = WSGIServerThread(self.app, self.host, self.port)
        self.server.start()
        self.server.wait_for_start()

    def stop(self):
        self.server.shutdown()
