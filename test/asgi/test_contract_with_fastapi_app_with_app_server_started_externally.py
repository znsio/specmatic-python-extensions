import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.servers.asgi_app_server import ASGIAppServer
from specmatic.coverage.servers.fastapi_app_coverage_server import FastApiAppCoverageServer
from specmatic.utils import get_project_root
from test.apps.fast_api import app

PROJECT_ROOT = get_project_root()

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 8080

expectation_json_file = PROJECT_ROOT + '/test/resources/data/expectation.json'
app_module = PROJECT_ROOT + '/test/sanic_app'

app_server = ASGIAppServer('test.apps.fast_api:app', app_host, app_port)
app_server.start()


class TestContract:
    pass


Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .test_with_api_coverage_for_fastapi_app(TestContract, app, app_host, app_port) \
    .run()

app_server.stop()

if __name__ == '__main__':
    pytest.main()
