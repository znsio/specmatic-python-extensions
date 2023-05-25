import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.utils import get_project_root
from test.sanic_app import app

PROJECT_ROOT = get_project_root()

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 8080

expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'


class TestContract:
    pass


stub = None
app_server = None
try:
    stub = Specmatic.start_stub(PROJECT_ROOT, stub_host, stub_port)
    stub.set_expectations([expectation_json_file])

    app_server = Specmatic.start_asgi_app(app, app_host, app_port)

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
