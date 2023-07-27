from abc import ABC, abstractmethod
from typing import List

from specmatic.actuator.actuator_route import ActuatorRoute


class AppRouteAdapter(ABC):
    @abstractmethod
    def to_actuator_routes(self) -> List[ActuatorRoute]:
        pass

    def process_route(self, route_url, methods) -> ActuatorRoute:
        print(f"\nStarted adapting route: {route_url} with methods: {methods}")
        methods = [method for method in methods if method != 'OPTIONS']
        if len(methods) > 1 and 'HEAD' in methods:
            methods = [method for method in methods if method != 'HEAD']
        if methods:
            print(f"Result: url: {route_url}, methods: [" + " ".join(methods) + "]")
            return ActuatorRoute(route_url, methods)
