import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.utils import get_project_root
from test.flask_app import app

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
PROJECT_ROOT = get_project_root()
expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'


class TestContract:
    pass


Specmatic.test_wsgi_app(app,
                        TestContract,
                        project_root=PROJECT_ROOT,
                        stub_host=stub_host,
                        stub_port=stub_port,
                        expectation_files=[expectation_json_file])

if __name__ == '__main__':
    pytest.main()
