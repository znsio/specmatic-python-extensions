from typing import List

from flask import Flask, jsonify

from specmatic.actuator.app_route_adapter import AppRouteAdapter
from specmatic.actuator.spring_actuator_route import SpringActuatorRoute
from specmatic.servers.wsgi_app_server import WSGIAppServer


class CoverageServer:
    def __init__(self, app_route_adapter: AppRouteAdapter):
        self.routes = app_route_adapter.to_actuator_routes()
        self.coverage_server_url = ""
        app = self.setup_coverage_flask_app()
        self.app_server = WSGIAppServer(app)

    def setup_coverage_flask_app(self):
        app = Flask(__name__)

        @app.route('/actuator/mappings', methods=['GET'])
        def generate_actuator_mappings_endpoint_response():
            response = {
                "contexts": {
                    "application": {
                        "mappings": {
                            "dispatcherServlets": {
                                "dispatcherServlet": []
                            }
                        }
                    }
                }
            }

            for route in self.routes:
                response['contexts']['application']['mappings']['dispatcherServlets']['dispatcherServlet'].append({
                    "details": {
                        "requestMappingConditions": {
                            "methods": route.methods,
                            "patterns": [route.url]
                        }
                    }
                })
            print("\nResponse from actuator route:")
            print(response)
            return jsonify(response)

        return app

    def start(self):
        print("\nStarting coverage server...")
        self.app_server.start()
        self.coverage_server_url = f"http://{self.app_server.host}:{self.app_server.app_port}"
        print(f"\nCoverage server started on: {self.coverage_server_url}")

    @property
    def endpoints_api(self):
        return f"{self.coverage_server_url}/actuator/mappings"

    def stop(self):
        print("\nStopping coverage server...")
        self.app_server.stop()
