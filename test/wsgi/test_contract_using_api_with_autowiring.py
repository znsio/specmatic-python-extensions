import os

import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.servers.wsgi_app_server import WSGIAppServer
from specmatic.utils import get_project_root
from test.apps.flask_app import app
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

app_server = WSGIAppServer(app, set_app_config_func=update_app_config_with_stub_info,
                           reset_app_config_func=reset_app_config)
Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .stub(expectations=[expectation_json_file]) \
    .app(app_server) \
    .test(TestContract) \
    .run()

if __name__ == '__main__':
    pytest.main()
