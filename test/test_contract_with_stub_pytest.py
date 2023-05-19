import pytest

from specmatic.core.decorators import specmatic_contract_test, specmatic_stub
from specmatic.utils import get_project_root

host = "127.0.0.1"
port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
expectation_json_file = get_project_root() + '/test/data/expectation.json'
service_contract_file = get_project_root() + '/test/spec/product-search-bff-api.yaml'
stub_contract_file = get_project_root() + '/test/spec/api_order_v1.yaml'


@specmatic_contract_test(host, port)
@specmatic_stub(stub_host, stub_port, [expectation_json_file])
class TestApiContract:
    @classmethod
    def teardown_class(cls):
        cls.stub.stop()


if __name__ == '__main__':
    pytest.main()
