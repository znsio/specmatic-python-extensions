import json
import subprocess
from time import sleep

import pytest

from specmatic_python.specmatic.decorators import specmatic_contract_test, specmatic_stub
from specmatic_python.utils import get_project_root

host = "127.0.0.1"
port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
expectation_json_file = get_project_root() + '/test/data/expectation.json'


@specmatic_contract_test(host, port)
@specmatic_stub(stub_host, stub_port, [expectation_json_file])
class TestApiContract:
    @classmethod
    def teardown_class(cls):
        cls.stub.stop()


if __name__ == '__main__':
    pytest.main()
