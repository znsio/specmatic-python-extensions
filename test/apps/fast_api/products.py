import requests
from test.apps.fast_api import configuration


class Products:
    def __init__(self):
        self.products_api = f'http://{configuration["ORDER_API_HOST"]}:{configuration["ORDER_API_PORT"]}/products'

    def search(self, product_type: str):
        try:
            return requests.get(self.products_api, params={'type': product_type})
        except requests.exceptions.RequestException as e:
            print(f'An error occurred while connecting to {self.products_api}', e)
            raise Exception(f'An error occurred while connecting to {self.products_api}' + str(e))
