import requests


class Products:
    products_api = 'http://127.0.0.1:8080/products'

    def search(self, product_type: str):
        try:
            return requests.get(self.products_api, params={'type': product_type})
        except requests.exceptions.RequestException as e:
            print(f'An error occurred while connecting to {self.products_api}', e)
            raise Exception(f'An error occurred while connecting to {self.products_api}' + str(e))
