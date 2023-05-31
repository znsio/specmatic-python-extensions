import pytest

from specmatic.core.specmatic import Specmatic
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

Specmatic.test_wsgi_app(app,
                        TestContract,
                        app_contracts=[app_contract_file],
                        stub_contracts=[stub_contract_file],
                        app_host=app_host,
                        app_port=app_port,
                        stub_host=stub_host,
                        stub_port=stub_port,
                        expectation_files=[expectation_json_file])

if __name__ == '__main__':
    pytest.main()