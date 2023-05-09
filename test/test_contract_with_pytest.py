import pytest

from specmaticpython.specmatic.specmatic_server import SpecmaticServer
from specmaticpython.utils import get_project_root

host = "127.0.0.1"
port = 5000


class TestContract:
    pass


SpecmaticServer() \
    .with_api_under_test_at(host, port) \
    .with_specmatic_json_at(get_project_root() + '/specmatic.json') \
    .configure_py_tests(TestContract)

if __name__ == '__main__':
    pytest.main()
