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


def set_app_config(app, host: str, port: int):
    app.config['ORDER_API_HOST'] = host
    app.config['ORDER_API_PORT'] = str(port)


def reset_app_config(app):
    app.config["ORDER_API_HOST"] = os.getenv("ORDER_API_HOST")
    app.config["ORDER_API_PORT"] = os.getenv("ORDER_API_PORT")


download_specmatic_jar_if_does_not_exist()

Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(expectations=[expectation_json_file]) \
    .with_app(app) \
    .with_set_app_config_func(set_app_config) \
    .with_reset_app_config_func(reset_app_config) \
    .test(TestContract) \
    .run()

if __name__ == '__main__':
    pytest.main()
