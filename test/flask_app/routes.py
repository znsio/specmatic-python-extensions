from flask_restful import Api
from test.flask_app import app
from test.flask_app.models import Product, Order

api = Api(app)

api.add_resource(Product, '/findAvailableProducts')
api.add_resource(Order, '/orders')
