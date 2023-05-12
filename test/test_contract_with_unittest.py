import unittest

from specmatic_python.specmatic.decorators import specmatic_contract_test
from specmatic_python.utils import get_project_root

host = "127.0.0.1"
port = 5000
specmatic_json_file = get_project_root() + '/specmatic.json'


@specmatic_contract_test(host, port, specmatic_json_file)
class TestContractUnitTest(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
