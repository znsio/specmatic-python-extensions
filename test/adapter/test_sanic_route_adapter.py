import unittest

from specmatic.coverage.sanic_app_route_adapter import SanicAppRouteAdapter
from test.apps.sanic_app import app
from test.adapter import VALID_COVERAGE_LIST

# NOTE: This adjustment is necessary due to the inconsistent ordering of route methods in Sanic (Only?).
VALID_COVERAGE_LIST = [(cov.url, sorted(cov.methods)) for cov in VALID_COVERAGE_LIST]


class TestSanicRouteAdapter(unittest.TestCase):
    def test_handles_no_converters(self):
        adapter = SanicAppRouteAdapter(app)
        routes = [
            (cov.url, sorted(cov.methods)) for cov in adapter.to_coverage_routes()
        ]
        self.assertCountEqual(routes, VALID_COVERAGE_LIST)
