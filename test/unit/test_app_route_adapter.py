from typing import List

import pytest

from specmatic.coverage.app_route_adapter import AppRouteAdapter
from specmatic.coverage.coverage_route import CoverageRoute


class DummyAdapter(AppRouteAdapter):

    def to_coverage_routes(self) -> List[CoverageRoute]:
        pass


class TestAppRouteAdapter:
    def test_handles_duplicate_route_with_trailing_slash(self):
        adapter = DummyAdapter([])
        adapter.process_route("/route1", ["GET"])
        adapter.process_route("/route1/", ["GET"])
        assert adapter.routes_as_list() == [CoverageRoute("/route1", ["GET"])]

    def test_handles_multiple_methods_with_routes_with_trailing_slash(self):
        adapter = DummyAdapter([])
        adapter.process_route("/route1", ["GET"])
        adapter.process_route("/route1/", ["GET"])
        adapter.process_route("/route1", ["POST"])
        adapter.process_route("/route1/", ["POST"])
        adapter.process_route("/route1", ["PUT"])
        adapter.process_route("/route1/", ["PUT"])
        adapter.process_route("/route1", ["DELETE"])
        adapter.process_route("/route1/", ["DELETE"])
        assert adapter.routes_as_list() == [CoverageRoute("/route1", ["GET", "POST", "PUT", "DELETE"])]
