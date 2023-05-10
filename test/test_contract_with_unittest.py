import unittest

from specmatic_python.specmatic.specmatic_server import SpecmaticServer
from specmatic_python.utils import get_project_root

host = "127.0.0.1"
port = 5000


class TestContractUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


SpecmaticServer() \
    .with_api_under_test_at(host, port) \
    .with_contract_file(get_project_root() + '/order_api_spec.yaml') \
    .configure_unit_tests(TestContractUnitTest)

if __name__ == '__main__':
    unittest.main()
