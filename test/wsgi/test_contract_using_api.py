import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.core.specmatic import Specmatic
from specmatic.servers.wsgi_app_server import WSGIAppServer
from specmatic.utils import get_project_root
from test.flask_app import app
from test.utils import download_specmatic_jar_if_does_not_exist

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
PROJECT_ROOT = get_project_root()
expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'
app_contract_file = PROJECT_ROOT + '/test/spec/product-search-bff-api.yaml'
stub_contract_file = PROJECT_ROOT + '/test/spec/api_order_v1.yaml'


class TestContract:
    pass


download_specmatic_jar_if_does_not_exist()

app_server = WSGIAppServer(app, app_host, app_port)
Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_test_class(TestContract) \
    .stub(stub_host, stub_port, [expectation_json_file]) \
    .app(app_server) \
    .test() \
    .run()

if __name__ == '__main__':
    pytest.main()
