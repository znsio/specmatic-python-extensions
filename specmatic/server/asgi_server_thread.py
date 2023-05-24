import threading
import uvicorn
import logging


class ASGIServerThread(threading.Thread):

    def __init__(self, app, host: str, port: int):
        threading.Thread.__init__(self)
        self.app = app
        self.host = host
        self.port = port
        self.daemon = True
        log_file_path = "uvicorn.log"  # Replace with the desired path for the log file
        logging.basicConfig(filename=log_file_path)
        server = uvicorn.Server(uvicorn.Config(self.app, host=self.host, port=self.port, log_level="info"))
        self.server = server

    def run(self):
        self.server.run()

    def shutdown(self):
        self.server.shutdown()
