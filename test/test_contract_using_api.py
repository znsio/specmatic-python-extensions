import pytest
from specmatic.core.specmatic import Specmatic
from specmatic.server.wsgi_server import WSGIServer
from specmatic.utils import get_project_root
from test.flask_app import app

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
PROJECT_ROOT = get_project_root()
expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'


class TestContract:
    pass


stub = None
app_server = None

try:
    stub = Specmatic.start_stub(PROJECT_ROOT, stub_host, stub_port)
    stub.set_expectations([expectation_json_file])

    app_server = WSGIServer(app, app_host, app_port)
    app_server.start()

    Specmatic.test(PROJECT_ROOT, TestContract, app_host, app_port)
except Exception as e:
    print(f"Error: {e}")
    raise e
finally:
    if app_server is not None:
        app_server.stop()
    if stub is not None:
        stub.stop()

if __name__ == '__main__':
    pytest.main()
