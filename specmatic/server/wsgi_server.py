from specmatic.server.server_thread import ServerThread


class WSGIServer:
    server: ServerThread = None

    def __init__(self, app, host: str, port: int):
        self.app = app
        self.host = host
        self.port = port

    def start(self):
        self.server = ServerThread(self.app, self.host, self.port)
        self.server.start()

    def stop(self):
        self.server.shutdown()
