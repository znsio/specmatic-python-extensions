import json

import requests


class Orders:
    orders_api = 'http://127.0.0.1:8080/orders'

    def create(self, order):
        # Set the headers to specify that we're sending JSON data
        headers = {
            "Content-Type": "application/json"
        }

        return requests.post(self.orders_api, json=order, headers=headers)
