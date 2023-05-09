import threading

from flask import Flask
from werkzeug.serving import make_server


class ServerThread(threading.Thread):

    def __init__(self, app: Flask, host: str, port: int):
        threading.Thread.__init__(self)
        self.server = make_server(host, port, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        print('Starting flask server...')
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()
