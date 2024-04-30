import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.servers.wsgi_app_server import WSGIAppServer
from specmatic.utils import get_project_root
from test.apps.flask import app

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
PROJECT_ROOT = get_project_root()
expectation_json_file = PROJECT_ROOT + '/test/resources/data/expectation.json'

app_server = WSGIAppServer(app, app_host, app_port)
app_server.start()


class TestContract:
    pass


Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .test_with_api_coverage_for_flask_app(TestContract, app, app_host, app_port) \
    .run()

app_server.stop()

if __name__ == '__main__':
    pytest.main()
