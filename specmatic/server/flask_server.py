from flask import Flask

from specmatic.server.server_thread import ServerThread


class FlaskServer:
    server: ServerThread = None

    def __init__(self, app: Flask, host: str, port: int):
        self.app = app
        self.host = host
        self.port = port

    def start(self):
        self.server = ServerThread(self.app, self.host, self.port)
        self.server.start()
        print(f'Flask server started on {self.host}:{self.port}')

    def stop(self):
        self.server.shutdown()
