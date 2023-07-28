from flask_restful import Api
from test.apps.flask import app
from test.apps.flask.models import ProductList, Order, Product

api = Api(app)

api.add_resource(ProductList, '/findAvailableProducts')
api.add_resource(Product, '/orders/<int:order_id>')
api.add_resource(Order, '/orders')
