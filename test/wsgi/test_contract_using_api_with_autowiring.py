import os

import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.utils import get_project_root
from test.flask_app import app
from test.utils import download_specmatic_jar_if_does_not_exist

stub_host = "127.0.0.1"
stub_port = 8080
PROJECT_ROOT = get_project_root()
expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'


class TestContract:
    pass


def update_app_config_with_stub_info(app, host: str, port: int):
    app.config['ORDER_API_HOST'] = host
    app.config['ORDER_API_PORT'] = str(port)


def reset_app_config(app):
    app.config["ORDER_API_HOST"] = os.getenv("ORDER_API_HOST")
    app.config["ORDER_API_PORT"] = os.getenv("ORDER_API_PORT")


download_specmatic_jar_if_does_not_exist()

Specmatic.test_wsgi_app(app,
                        TestContract,
                        project_root=PROJECT_ROOT,
                        expectation_files=[expectation_json_file],
                        app_config_update_func=update_app_config_with_stub_info)

reset_app_config(app)

if __name__ == '__main__':
    pytest.main()
