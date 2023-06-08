import unittest

from specmatic.core.specmatic import Specmatic
from specmatic.servers.wsgi_app_server import WSGIAppServer
from specmatic.utils import get_project_root
from test.apps.flask_app import app
from test.utils import download_specmatic_jar_if_does_not_exist

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
PROJECT_ROOT = get_project_root()
expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'


class TestContract(unittest.TestCase):
    pass


download_specmatic_jar_if_does_not_exist()

app_server = WSGIAppServer(app, app_host, app_port)
Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .stub(stub_host, stub_port, [expectation_json_file]) \
    .app(app_server) \
    .test(TestContract) \
    .run()

if __name__ == '__main__':
    unittest.main()
