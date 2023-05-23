import pytest

from specmatic.core.decorators import specmatic_contract_test, specmatic_stub, start_app
from specmatic.core.specmatic import Specmatic
from specmatic.server.wsgi_server import WSGIServer
from specmatic.utils import get_project_root
from test.api import app

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
expectation_json_file = get_project_root() + '/test/data/expectation.json'


class TestApiContract:
    pass


stub = Specmatic() \
    .stub(stub_host, stub_port) \
    .build()
stub.start()
stub.set_expectations([expectation_json_file])

wsgi_app = WSGIServer(app, app_host, app_port)
wsgi_app.start()

Specmatic() \
    .test(app_host, app_port) \
    .configure_py_tests(TestApiContract)

wsgi_app.stop()
stub.stop()

if __name__ == '__main__':
    pytest.main(['v', 's'])
