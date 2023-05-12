import json
import subprocess
from time import sleep

import pytest

from specmatic_python.specmatic.decorators import run_specmatic, create_stub
from specmatic_python.utils import get_project_root

host = "127.0.0.1"
port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
specmatic_json_file = get_project_root() + '/specmatic.json'
expectation_json_file = get_project_root() + '/test/data/expectation.json'


@run_specmatic(host, port, specmatic_json_file)
@create_stub(stub_host, stub_port, specmatic_json_file, expectation_json_file)
class TestApiContract:
    @classmethod
    def teardown_class(cls):
        cls.stub.stop()


if __name__ == '__main__':
    pytest.main()
