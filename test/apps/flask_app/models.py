from test.apps.db.Orders import Orders
from test.apps.db.Products import Products
from flask_restful import Resource
from flask import request
import json


class ProductList(Resource):
    def get(self):
        product_type = request.args.get('type')
        if product_type is None:
            return {'message': 'The "type" parameter is mandatory.'}, 400

        response = Products().search(product_type)
        if response.status_code != 200:
            return {'message': 'An error occurred while retrieving the products.'}, response.status_code

        product_list = json.loads(response.content)

        products = [
            {"id": product["id"], "name": product["name"], "type": product["type"], "inventory": product["inventory"]}
            for product in product_list]
        return products


class Product(Resource):
    # Dummy route for actuator testing
    def get(self, product_id):
        return {"id": product_id, "name": "Product", "type": "gadget", "inventory": 10}


class Order(Resource):
    def post(self):
        order = request.get_json()
        order["status"] = "pending"
        response = Orders().create(order)
        if response.status_code != 200:
            return {'message': 'An error occurred while creating the order.'}, response.status_code
        order_response = json.loads(response.content)
        return {order_response['id']: 'success'}
