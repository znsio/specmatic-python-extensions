import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.utils import get_project_root

PROJECT_ROOT = get_project_root()

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 8080

expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'
service_contract_file = PROJECT_ROOT + '/test/spec/product-search-bff-api.yaml'
stub_contract_file = PROJECT_ROOT + '/test/spec/api_order_v1.yaml'
app_module = PROJECT_ROOT + '/test/sanic_app'


class TestContract:
    pass


stub = None
app_server = None
try:
    stub = Specmatic.start_stub(stub_host, stub_port, contract_file_path=stub_contract_file)
    stub.set_expectations([expectation_json_file])

    app_server = Specmatic.start_asgi_app('test.sanic_app:app', app_host, app_port)

    Specmatic.test(TestContract, app_host, app_port, contract_file_path=service_contract_file)
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
