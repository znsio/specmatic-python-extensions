import os

import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.utils import get_project_root
from test.apps.flask_app import app
from test.utils import download_specmatic_jar_if_does_not_exist

stub_host = "127.0.0.1"
stub_port = 8080
PROJECT_ROOT = get_project_root()
expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'


class TestContract:
    pass


download_specmatic_jar_if_does_not_exist()

os.environ['SPECMATIC_GENERATIVE_TESTS'] = 'True'

Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .with_app(app) \
    .test(TestContract) \
    .run()

os.environ['SPECMATIC_GENERATIVE_TESTS'] = 'False'

if __name__ == '__main__':
    pytest.main()
