import pytest
from specmatic.core.specmatic import Specmatic

from test.sanic_app import app
from specmatic.utils import get_project_root
from specmatic.server.asgi_server import ASGIServer

PROJECT_ROOT = get_project_root()

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 8080

expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'


class TestContract:
    pass


stub = Specmatic.start_stub(PROJECT_ROOT, stub_host, stub_port)
stub.set_expectations([expectation_json_file])

app_server = ASGIServer(app, app_host, app_port)
app_server.start()

Specmatic.test(PROJECT_ROOT, TestContract, app_host, app_port)

app_server.stop()
stub.stop()

if __name__ == '__main__':
    pytest.main()
