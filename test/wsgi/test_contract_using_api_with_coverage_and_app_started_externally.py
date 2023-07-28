import pytest

from specmatic.actuator.flask_app_route_adapter import FlaskAppRouteAdapter
from specmatic.core.specmatic import Specmatic
from specmatic.servers.coverage_server import CoverageServer
from specmatic.servers.wsgi_app_server import WSGIAppServer
from specmatic.utils import get_project_root
from test.apps.flask import app

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
PROJECT_ROOT = get_project_root()
expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'


class TestContract:
    pass


app_server = WSGIAppServer(app, app_host, app_port)
coverage_server = CoverageServer(FlaskAppRouteAdapter(app))

app_server.start()
coverage_server.start()

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
