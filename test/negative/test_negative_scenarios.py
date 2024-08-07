import socket

import pytest

from specmatic.core.specmatic import Specmatic
from specmatic.utils import find_available_port
from test import ROOT_DIR, expectation_json_files

app_host = "127.0.0.1"
app_port = 8000
stub_host = "127.0.0.1"
stub_port = 8080

invalid_expectation_json_file = ROOT_DIR + "/test/data/invalid_expectation.json"


class TestNegativeScenarios:
    def test_throws_exception_and_shuts_down_stub_when_stub_port_is_already_in_use(
        self,
    ):
        with pytest.raises(Exception) as exception:
            random_free_port = find_available_port()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(("localhost", random_free_port))
            Specmatic().with_project_root(ROOT_DIR).with_stub(
                "127.0.0.1", random_free_port
            ).run()
            sock.close()
        assert (
            f"{exception.value}".find("Stub process terminated due to an error") != -1
        )

    def test_throws_exception_when_expectation_json_is_invalid(self):
        with pytest.raises(Exception) as exception:
            Specmatic().with_project_root(ROOT_DIR).with_stub(
                expectations=[invalid_expectation_json_file]
            ).with_asgi_app("test.apps.sanic_app:app").test(TestNegativeScenarios).run()
        assert f"{exception.value}".find("No match was found") != -1

    def test_throws_exception_when_app_module_is_invalid(self):
        with pytest.raises(Exception) as exception:
            Specmatic().with_asgi_app("main:app").with_project_root(ROOT_DIR).test(
                TestNegativeScenarios
            ).run()
        assert f"{exception.value}".find("App process terminated due to an error") != -1


if __name__ == "__main__":
    pytest.main()
