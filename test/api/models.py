from test.db.Orders import Orders
from test.db.Products import Products
from flask_restful import Resource
from flask import request
import json


class Product(Resource):
    def get(self):
        product_type = request.args.get('type')
        if product_type is None:
            return {'message': 'The "type" parameter is mandatory.'}, 400

        response = Products().search(product_type)
        if response.status_code != 200:
            return {'message': 'An error occurred while retrieving the products.'}, response.status_code

        product_list = json.loads(response.content)

        products = [{"id": product["id"], "name": product["name"]} for product in product_list]
        return products


class Order(Resource):
    def post(self):
        order = request.get_json()
        order["status"] = "pending"
        response = Orders().create(order)
        if response.status_code != 200:
            return {'message': 'An error occurred while creating the order.'}, response.status_code
        order_response = json.loads(response.content)
        return {order_response['id']: 'success'}
