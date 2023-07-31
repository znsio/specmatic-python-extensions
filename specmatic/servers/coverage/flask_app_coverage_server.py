from specmatic.actuator.flask_app_route_adapter import FlaskAppRouteAdapter
from specmatic.servers.coverage.coverage_server import CoverageServer


class FlaskAppCoverageServer(CoverageServer):
    def __init__(self, app):
        super().__init__(FlaskAppRouteAdapter(app))
