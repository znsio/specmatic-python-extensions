import re
from typing import List

from specmatic.actuator.app_route_adapter import AppRouteAdapter
from specmatic.actuator.spring_actuator_route import SpringActuatorRoute


class SanicAppRouteAdapter(AppRouteAdapter):
    def __init__(self, app):
        self.app = app

    def to_actuator_routes(self) -> List[SpringActuatorRoute]:
        routes = []
        for route in self.app.router.routes_all.values():
            if route.uri != 'static':  # Exclude static routes
                route_url = route.uri
                methods = route.methods
                print(f"\nStarted adapting route: {route_url} with methods: {methods}")
                methods = [method for method in methods if method != 'OPTIONS']
                if len(methods) > 1 and 'HEAD' in methods:
                    methods = [method for method in methods if method != 'HEAD']
                if methods:
                    url = self.convert_sanic_route_url_to_spring_actuator_format(route_url)
                    routes.append(SpringActuatorRoute(url, methods))
                    print(f"Result: url: {url}, methods: [" + " ".join(methods) + "]")
        return routes

    def convert_sanic_route_url_to_spring_actuator_format(self, flask_route_url):
        pattern = r'<(\w+):(\w+)>'
        return re.sub(pattern, r'{\1}', flask_route_url)
