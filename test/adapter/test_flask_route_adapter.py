import unittest

from specmatic.coverage.flask_app_route_adapter import FlaskAppRouteAdapter
from test.apps.flask_app import app
from test.adapter import VALID_COVERAGE_LIST


class TestFlaskRouteAdapter(unittest.TestCase):
    def test_handles_no_converters(self):
        adapter = FlaskAppRouteAdapter(app)
        routes = adapter.to_coverage_routes()
        self.assertListEqual(routes, VALID_COVERAGE_LIST)
