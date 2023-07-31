from specmatic.actuator.sanic_app_route_adapter import SanicAppRouteAdapter
from specmatic.servers.coverage.coverage_server import CoverageServer


class SanicAppCoverageServer(CoverageServer):
    def __init__(self, app):
        super().__init__(SanicAppRouteAdapter(app))
