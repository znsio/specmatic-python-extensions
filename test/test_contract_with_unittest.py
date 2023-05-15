import unittest

from specmatic.core.decorators import specmatic_contract_test
from specmatic.utils import get_project_root

host = "127.0.0.1"
port = 5000

@specmatic_contract_test(host, port)
class TestContractUnitTest(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
