import requests
from test.api import app


class Orders:
    def __init__(self):
        self.orders_api = f'http://{app.config["ORDER_API_HOST"]}:{app.config["ORDER_API_PORT"]}/orders'

    def create(self, order):
        # Set the headers to specify that we're sending JSON data
        headers = {
            "Content-Type": "application/json"
        }

        return requests.post(self.orders_api, json=order, headers=headers)
