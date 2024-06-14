import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.utils import get_project_root
from test.apps.sanic import app

PROJECT_ROOT = get_project_root()

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 8080

expectation_json_file = PROJECT_ROOT + '/test/resources/data/expectation.json'


class TestContract:
    pass


Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .with_asgi_app('test.apps.sanic:app', app_host, app_port) \
    .test_with_api_coverage_for_sanic_app(TestContract, app) \
    .run()

if __name__ == '__main__':
    pytest.main()
