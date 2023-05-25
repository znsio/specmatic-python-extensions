import pytest

from specmatic.core.decorators import specmatic_contract_test, specmatic_stub, start_app
from specmatic.utils import get_project_root
from test.flask_app import app

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
PROJECT_ROOT = get_project_root()
APP_ROOT = PROJECT_ROOT + '/test'
expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'


@specmatic_contract_test(project_root=PROJECT_ROOT)
@start_app(app)
@specmatic_stub(stub_host, stub_port, PROJECT_ROOT, [expectation_json_file])
class TestContract:
    pass


if __name__ == '__main__':
    pytest.main()
