import re
from typing import List

from specmatic.actuator.app_route_adapter import AppRouteAdapter
from specmatic.actuator.spring_actuator_route import SpringActuatorRoute


class FlaskAppRouteAdapter(AppRouteAdapter):
    def __init__(self, app):
        self.app = app

    def to_actuator_routes(self) -> List[SpringActuatorRoute]:
        routes = []
        for route in self.app.url_map.iter_rules():
            if route.endpoint != 'static':  # Exclude static routes
                route_url = str(route)
                methods = route.methods
                print(f"\nStarted adapting route: {route_url} with methods: {methods}")
                methods = [method for method in methods if method != 'OPTIONS']
                print(f"Removing the 'OPTIONS' method if present")
                if len(methods) > 1 and 'HEAD' in methods:
                    print(f"Removing the 'HEAD' method which is auto-added by Flask")
                    methods = [method for method in methods if method != 'HEAD']
                if methods:
                    url = self.convert_flask_route_url_to_spring_actuator_format(str(route))
                    print(f"Route in Spring Actuator Format: {url}")
                    routes.append(SpringActuatorRoute(url, methods))
                    print(f"Result: url: {url}, methods: [" + " ".join(methods) + "]")
        return routes

    def convert_flask_route_url_to_spring_actuator_format(self, flask_route_url):
        pattern = r'<\w+:(\w+)>'
        return re.sub(pattern, r'{\1}', flask_route_url)
