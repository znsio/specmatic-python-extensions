import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.servers.asgi_app_server import ASGIAppServer
from specmatic.coverage.servers.sanic_app_coverage_server import SanicAppCoverageServer
from specmatic.utils import get_project_root
from test.apps.sanic import app

PROJECT_ROOT = get_project_root()

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 8080

expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'
app_module = PROJECT_ROOT + '/test/sanic_app'

app_server = ASGIAppServer('test.apps.sanic:app', app_host, app_port)
coverage_server = SanicAppCoverageServer(app)

app_server.start()
coverage_server.start()


class TestContract:
    pass


Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .with_endpoints_api(coverage_server.endpoints_api) \
    .test(TestContract, app_host, app_port) \
    .run()

app_server.stop()
coverage_server.stop()

if __name__ == '__main__':
    pytest.main()
