import os

import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.utils import get_project_root
from test.flask_app import app

stub_host = "127.0.0.1"
stub_port = 8080
PROJECT_ROOT = get_project_root()
expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'


class TestContract:
    pass


stub = None
app_server = None
try:
    stub = Specmatic.start_stub(project_root=PROJECT_ROOT)
    stub.set_expectations([expectation_json_file])

    app.config['ORDER_API_HOST'] = stub.host
    app.config['ORDER_API_PORT'] = stub.port
    app_server = Specmatic.start_wsgi_app(app)

    Specmatic.test(TestContract, app_server.host, app_server.port, PROJECT_ROOT)
except Exception as e:
    print(f"Error: {e}")
    raise e
finally:
    app.config["ORDER_API_HOST"] = os.getenv("ORDER_API_HOST")
    app.config["ORDER_API_PORT"] = os.getenv("ORDER_API_PORT")
    if app_server is not None:
        app_server.stop()
    if stub is not None:
        stub.stop()

if __name__ == '__main__':
    pytest.main()
