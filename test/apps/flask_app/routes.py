from flask_restful import Api
from test.apps.flask_app import app
from test.apps.flask_app.models import Product, Order

api = Api(app)

api.add_resource(Product, '/findAvailableProducts')
api.add_resource(Order, '/orders')
