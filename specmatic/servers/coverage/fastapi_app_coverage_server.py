from specmatic.actuator.fastapi_app_route_adapter import FastApiAppRouteAdapter
from specmatic.servers.coverage.coverage_server import CoverageServer


class FastApiAppCoverageServer(CoverageServer):
    def __init__(self, app):
        super().__init__(FastApiAppRouteAdapter(app))
