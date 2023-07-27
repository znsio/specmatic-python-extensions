import re
from typing import List

from specmatic.actuator.app_route_adapter import AppRouteAdapter
from specmatic.actuator.actuator_route import ActuatorRoute


class FlaskAppRouteAdapter(AppRouteAdapter):
    def __init__(self, app):
        self.app = app

    def to_actuator_routes(self) -> List[ActuatorRoute]:
        routes = []
        for route in self.app.url_map.iter_rules():
            if route.endpoint != 'static':  # Exclude static routes
                route_url = self.convert_to_spring_actuator_format(str(route))
                methods = route.methods
                routes.append(self.process_route(route_url, methods))
        return routes

    def convert_to_spring_actuator_format(self, flask_route_url):
        pattern = r'<\w+:(\w+)>'
        return re.sub(pattern, r'{\1}', flask_route_url)
