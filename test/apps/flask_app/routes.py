from flask_restful import Api
from test.apps.flask_app import app
from test.apps.flask_app.models import ProductList, Order, Product

api = Api(app)

api.add_resource(ProductList, '/findAvailableProducts')
api.add_resource(Product, '/orders/<int:order_id>')
api.add_resource(Order, '/orders')
