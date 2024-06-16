import unittest

from specmatic.coverage.fastapi_app_route_adapter import FastApiAppRouteAdapter
from test.apps.fast_api import app
from test.adapter import VALID_COVERAGE_LIST


class TestFastApiRouteAdapter(unittest.TestCase):
    def test_handles_no_converters(self):
        adapter = FastApiAppRouteAdapter(app)
        routes = adapter.to_coverage_routes()
        self.assertListEqual(routes, VALID_COVERAGE_LIST)
