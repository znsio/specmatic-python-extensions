import re
from typing import List

from specmatic.coverage.app_route_adapter import AppRouteAdapter
from specmatic.coverage.coverage_route import CoverageRoute


class SanicAppRouteAdapter(AppRouteAdapter):
    def to_coverage_routes(self) -> List[CoverageRoute]:
        for route in self.app.router.routes:
            route_url = self.convert_to_spring_actuator_url_format(route.uri)
            methods = route.methods
            print(f"\nStarted adapting route: {route_url} with methods: {methods}")
            self.process_route(route_url, methods)
        return self.routes_as_list()

    def convert_to_spring_actuator_url_format(self, flask_route_url):
        pattern = r"<(\w+):([^\/]+)>"
        return re.sub(pattern, r"{\1}", flask_route_url)
