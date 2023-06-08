import inspect
import socket

import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.servers.asgi_app_server import ASGIAppServer
from specmatic.utils import get_project_root, find_available_port
from test.utils import download_specmatic_jar_if_does_not_exist

PROJECT_ROOT = get_project_root()

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 8080

expectation_json_file = PROJECT_ROOT + '/test/data/expectation.json'
invalid_expectation_json_file = PROJECT_ROOT + '/test/data/invalid_expectation.json'
app_module = PROJECT_ROOT + '/test/sanic_app'

download_specmatic_jar_if_does_not_exist()


class TestNegativeScenarios:

    def test_throws_exception_when_project_root_is_not_specified(self):
        with pytest.raises(Exception) as exception:
            Specmatic() \
                .with_stub(expectations=[expectation_json_file]) \
                .with_app_module('test.apps.sanic_app:app') \
                .test(TestNegativeScenarios) \
                .run()
        assert f"{exception.value}" == 'Please specify either of the following parameters: project_root, specmatic_json_file_path'

    def test_throws_exception_and_shuts_down_stub_when_specmatic_json_path_is_not_found(self):
        with pytest.raises(Exception) as exception:
            Specmatic() \
                .with_project_root(PROJECT_ROOT + '/wrong_path') \
                .with_stub(expectations=[expectation_json_file]) \
                .with_app_module('test.apps.sanic_app:app') \
                .test(TestNegativeScenarios) \
                .run()
        assert f"{exception.value}".find('Stub process terminated due to an error') != -1

    def test_throws_exception_and_shuts_down_stub_when_stub_port_is_already_in_use(self):
        with pytest.raises(Exception) as exception:
            random_free_port = find_available_port()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('localhost', random_free_port))
            Specmatic() \
                .with_project_root(PROJECT_ROOT) \
                .with_stub('127.0.0.1', random_free_port) \
                .run()
            sock.close()
        assert f"{exception.value}".find('Stub process terminated due to an error') != -1

    def test_throws_exception_when_expectation_json_is_invalid(self):
        with pytest.raises(Exception) as exception:
            Specmatic() \
                .with_project_root(PROJECT_ROOT) \
                .with_stub(expectations=[invalid_expectation_json_file]) \
                .with_app_module('test.apps.sanic_app:app') \
                .test(TestNegativeScenarios) \
                .run()
        assert f"{exception.value}".find('No match was found') != -1

    def test_throws_exception_when_app_module_is_invalid(self):
        with pytest.raises(Exception) as exception:
            Specmatic() \
                .with_project_root(PROJECT_ROOT) \
                .with_stub(expectations=[expectation_json_file]) \
                .with_app_module('main:app') \
                .test(TestNegativeScenarios) \
                .run()
        assert f"{exception.value}".find('App process terminated due to an error') != -1


if __name__ == '__main__':
    pytest.main()
