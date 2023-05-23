import sys
import threading
from werkzeug.serving import make_server
import logging


class WSGIServerThread(threading.Thread):

    def __init__(self, app, host: str, port: int):
        threading.Thread.__init__(self)
        logger = logging.getLogger("werkzeug")
        logger.addHandler(logging.StreamHandler(sys.stdout))
        print("Starting web server")
        self.server = make_server(host, port, app)
        self.server.log_startup()
        self.ctx = app.app_context()
        self.ctx.push()
        self.start_event = threading.Event()

    def wait_for_start(self):
        self.start_event.wait()

    def run(self):
        print("Web server started")
        self.start_event.set()
        self.server.serve_forever()


    def shutdown(self):
        self.server.shutdown()
