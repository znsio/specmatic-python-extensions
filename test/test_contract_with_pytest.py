import pytest

from specmatic_python.specmatic.specmatic import Specmatic
from specmatic_python.utils import get_project_root

host = "127.0.0.1"
port = 5000


class TestContract:
    pass


Specmatic() \
    .test(host, port) \
    .with_specmatic_json_at(get_project_root() + '/specmatic.json') \
    .configure_py_tests(TestContract)

if __name__ == '__main__':
    pytest.main()
