import pytest
import configparser

from specmatic.core.specmatic import Specmatic
from specmatic.servers.asgi_app_server import ASGIAppServer
from specmatic.utils import get_project_root
from test.utils import download_specmatic_jar_if_does_not_exist

PROJECT_ROOT = get_project_root()

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 8080

expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'
app_module = PROJECT_ROOT + '/test/sanic_app'

config_ini_path = get_project_root() + '/test/config.ini'


class TestContract:
    pass


def set_app_config(host: str, port: int):
    config = configparser.ConfigParser()
    config.read(config_ini_path)
    config['dev']['ORDER_API_HOST'] = host
    config['dev']['ORDER_API_PORT'] = str(port)
    with open(config_ini_path, 'w') as configfile:
        config.write(configfile)


def reset_app_config():
    config = configparser.ConfigParser()
    config.read(config_ini_path)
    config['dev']['ORDER_API_HOST'] = '127.0.0.1'
    config['dev']['ORDER_API_PORT'] = '8080'
    with open(config_ini_path, 'w') as configfile:
        config.write(configfile)


download_specmatic_jar_if_does_not_exist()


Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(expectations=[expectation_json_file]) \
    .with_app_module('test.apps.sanic_app:app') \
    .with_set_app_config_func(set_app_config) \
    .with_reset_app_config_func(reset_app_config) \
    .test(TestContract) \
    .run()

if __name__ == '__main__':
    pytest.main()
