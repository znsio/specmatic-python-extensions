from typing import List

from fastapi.routing import APIRoute

from specmatic.coverage.coverage_route import CoverageRoute
from specmatic.coverage.app_route_adapter import AppRouteAdapter


class FastApiAppRouteAdapter(AppRouteAdapter):
    def to_coverage_routes(self) -> List[CoverageRoute]:
        routes = []
        for route in self.app.routes:
            if isinstance(route, APIRoute):
                route_url = route.path
                methods = route.methods
                print(f"\nStarted adapting route: {route_url} with methods: {methods}")
                routes.append(self.process_route(route_url, methods))
        return routes
