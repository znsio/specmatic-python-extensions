from test.apps.sanic_app import app
from sanic.response import json
import json as jsonp

from test.apps.sanic_db.products import Products


@app.route("/findAvailableProducts", methods=["GET"])
async def get_products(request):
    product_type = request.args.get("type")
    if not product_type:
        return json({"error": "Missing 'type' query parameter"}, status=400)
    response = Products().search(product_type)
    if response.status_code != 200:
        return {'message': 'An error occurred while retrieving the products.'}, response.status_code

    product_list = jsonp.loads(response.content)

    products = [
        {"id": product["id"], "name": product["name"], "type": product["type"], "inventory": product["inventory"]} for
        product in product_list]
    return json(products)


# Dummy route for actuator testing
@app.route("/orders", methods=["POST"])
async def create_order(request):
    pass


# Dummy route for actuator testing
@app.route("/orders/<order_id:int>", methods=["GET"])
async def get_order(request):
    pass
