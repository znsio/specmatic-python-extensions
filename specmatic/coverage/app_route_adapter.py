from abc import ABC, abstractmethod
from typing import List

from specmatic.coverage.coverage_route import CoverageRoute


class AppRouteAdapter(ABC):
    def __init__(self, app):
        self.app = app

    @abstractmethod
    def to_coverage_routes(self) -> List[CoverageRoute]:
        pass

    def process_route(self, route_url, methods) -> CoverageRoute:
        methods = [method for method in methods if method != 'OPTIONS']
        if len(methods) > 1 and 'HEAD' in methods:
            methods = [method for method in methods if method != 'HEAD']
        if methods:
            print(f"Adapter result: url: {route_url}, methods: [" + " ".join(methods) + "]")
            return CoverageRoute(route_url, methods)
