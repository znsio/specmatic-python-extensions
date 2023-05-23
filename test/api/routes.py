from flask_restful import Api
from test.api import app
from test.api.models import Product, Order

api = Api(app)

api.add_resource(Product, '/findAvailableProducts')
api.add_resource(Order, '/orders')
