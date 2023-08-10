from abc import ABC, abstractmethod
from typing import List

from specmatic.coverage.coverage_route import CoverageRoute


class AppRouteAdapter(ABC):
    def __init__(self, app):
        self.app = app
        self.routes: List[CoverageRoute] = []

    @abstractmethod
    def to_coverage_routes(self) -> List[CoverageRoute]:
        pass

    def process_route(self, route_url, methods):
        route_url = self.remove_trailing_slash(route_url)
        if any(route.url == route_url for route in self.routes):
            print("Route has already been processed (possible duplicate due to present/missing trailing slash)")
        else:
            methods = [method for method in methods if method != 'OPTIONS']
            if len(methods) > 1 and 'HEAD' in methods:
                methods = [method for method in methods if method != 'HEAD']
            if methods:
                print(f"Adapter result: url: {route_url}, methods: [" + " ".join(methods) + "]")
                self.routes.append(CoverageRoute(route_url, methods))

    def remove_trailing_slash(app, route_url: str):
        if route_url.endswith("/") and route_url != "/":
            return route_url.rstrip("/")
        return route_url
