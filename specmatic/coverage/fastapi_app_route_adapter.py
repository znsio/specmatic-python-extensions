import re
from typing import List

from fastapi.routing import APIRoute

from specmatic.coverage.coverage_route import CoverageRoute
from specmatic.coverage.app_route_adapter import AppRouteAdapter


class FastApiAppRouteAdapter(AppRouteAdapter):
    def to_coverage_routes(self) -> List[CoverageRoute]:
        for route in self.app.routes:
            if isinstance(route, APIRoute):
                route_url = route.path
                methods = route.methods
                print(f"\nStarted adapting route: {route_url} with methods: {methods}")
                route_url = self.convert_to_spring_actuator_url_format(route_url)
                self.process_route(route_url, methods)
        return self.routes_as_list()

    def convert_to_spring_actuator_url_format(self, route_url):
        pattern = r":\w+(?=})"
        return re.sub(pattern, "", route_url)
