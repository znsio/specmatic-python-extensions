import json
import subprocess
from time import sleep

import pytest

from specmatic_python.specmatic.specmatic import Specmatic
from specmatic_python.utils import get_project_root

host = "127.0.0.1"
port = 5000


class TestApiContract:
    @classmethod
    def setupClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


stub = Specmatic()\
    .stub("127.0.0.1", 8080)\
    .with_specmatic_json_at(get_project_root() + '/specmatic.json')\
    .build()
stub.start()
sleep(5)
stub.set_expectation(get_project_root() + '/test/data/expectation.json')
Specmatic() \
    .test(host, port) \
    .with_specmatic_json_at(get_project_root() + '/specmatic.json') \
    .configure_py_tests(TestApiContract)
stub.stop()

if __name__ == '__main__':
    pytest.main()
