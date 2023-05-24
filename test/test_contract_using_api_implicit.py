import pytest
from specmatic.core.specmatic import Specmatic
from specmatic.server.wsgi_server import WSGIServer
from specmatic.utils import get_project_root
from test.api import app


stub_host = "127.0.0.1"
stub_port = 8080
PROJECT_ROOT = get_project_root()
expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'


class TestContract:
    pass


stub = Specmatic.start_stub(PROJECT_ROOT)
stub.set_expectations([expectation_json_file])

app.config['ORDER_API_HOST'] = stub.host
app.config['ORDER_API_PORT'] = stub.port
app_server = WSGIServer(app)
app_server.start()

Specmatic.test(PROJECT_ROOT, TestContract, app_server.host, app_server.port)

app_server.stop()
stub.stop()

if __name__ == '__main__':
    pytest.main()
