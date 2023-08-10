from abc import ABC, abstractmethod
from typing import List

from specmatic.coverage.coverage_route import CoverageRoute


class AppRouteAdapter(ABC):
    def __init__(self, app):
        self.app = app
        self.routes = {}

    @abstractmethod
    def to_coverage_routes(self) -> List[CoverageRoute]:
        pass

    def process_route(self, route_url, methods):
        route_url = self.remove_trailing_slash(route_url)
        methods = self.filter_methods(methods)
        if route_url in self.routes:
            existing_route_methods = self.routes[route_url]
            existing_route_methods.extend(method for method in methods if method not in existing_route_methods)
            self.routes[route_url] = existing_route_methods
        else:
            self.routes[route_url] = methods
        print(f"Adapter result: url: {route_url}, methods: [" + " ".join(methods) + "]")

    def remove_trailing_slash(self, route_url: str):
        if route_url.endswith("/") and route_url != "/":
            return route_url.rstrip("/")
        return route_url

    def filter_methods(self, methods):
        methods = [method for method in methods if method != 'OPTIONS']
        if len(methods) > 1 and 'HEAD' in methods:
            methods = [method for method in methods if method != 'HEAD']
        return methods

    def routes_as_list(self) -> List[CoverageRoute]:
        routes_list = []
        for key, value in self.routes.items():
            routes_list.append(CoverageRoute(key, value))
        return routes_list
