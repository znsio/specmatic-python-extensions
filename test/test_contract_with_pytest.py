import pytest

from specmatic.core.decorators import specmatic_contract_test, specmatic_stub, start_web_app
from specmatic.utils import get_project_root
from test.api import app

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
expectation_json_file = get_project_root() + '/test/data/expectation.json'


@specmatic_contract_test(app_host, app_port)
@start_web_app(app, app_host, app_port)
@specmatic_stub(stub_host, stub_port, [expectation_json_file])
class TestApiContract:
    @classmethod
    def teardown_class(cls):
        cls.web_app.stop()
        cls.stub.stop()


if __name__ == '__main__':
    pytest.main(['v', 's'])
