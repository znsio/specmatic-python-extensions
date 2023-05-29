import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.utils import get_project_root

PROJECT_ROOT = get_project_root()

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 8080

expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'
app_contract_file = PROJECT_ROOT + '/test/spec/product-search-bff-api.yaml'
stub_contract_file = PROJECT_ROOT + '/test/spec/api_order_v1.yaml'
app_module = PROJECT_ROOT + '/test/sanic_app'


class TestContract:
    pass


Specmatic.test_asgi_app('test.sanic_app:app',
                        TestContract,
                        app_contract_file=app_contract_file,
                        stub_contract_file=stub_contract_file,
                        app_host=app_host,
                        app_port=app_port,
                        stub_host=stub_host,
                        stub_port=stub_port,
                        expectation_files=[expectation_json_file])

if __name__ == '__main__':
    pytest.main()
