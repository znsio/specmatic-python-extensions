import subprocess

import pytest

from specmatic_python.specmatic.specmatic import Specmatic
from specmatic_python.utils import get_project_root

host = "127.0.0.1"
port = 5000


class TestApiContract:
    stub = None

    @classmethod
    def setupClass(cls):
        cls.stub = Specmatic.create_stub("127.0.0.1", 8080)
        cls.stub.start()

    @classmethod
    def tearDownClass(cls):
        cls.stub.stop()


Specmatic() \
    .test(host, port) \
    .with_specmatic_json_at(get_project_root() + '/specmatic.json')\
    .configure_py_tests(TestApiContract)

if __name__ == '__main__':
    pytest.main()
