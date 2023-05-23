import pytest

from specmatic.core.decorators import specmatic_contract_test, specmatic_stub, start_app
from specmatic.utils import get_project_root
from test.api import app

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
PROJECT_ROOT = get_project_root()
expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'
service_contract_file = PROJECT_ROOT + '/test/spec/product-search-bff-api.yaml'
stub_contract_file = PROJECT_ROOT + '/test/spec/api_order_v1.yaml'


@specmatic_contract_test(PROJECT_ROOT, app_host, app_port, service_contract_file)
@start_app(app, app_host, app_port)
@specmatic_stub(PROJECT_ROOT, stub_host, stub_port, [expectation_json_file], stub_contract_file)
class TestContractWithLocalSpecs:
    pass


if __name__ == '__main__':
    pytest.main()
