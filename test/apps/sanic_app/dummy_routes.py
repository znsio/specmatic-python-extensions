# Dummy Routes For Coverage Testing and Route-Adapter Testing
from sanic import Blueprint, text

dummy = Blueprint("dummy")


@dummy.route("/orders/<id>", methods=["GET"])
async def get_order(id):
    return text("dummy")


@dummy.route("/orders/<id:int>", methods=["PUT"])
async def update_order(id):
    return text("dummy")


@dummy.route("/orders/<id:([1-9]{1,})>", methods=["DELETE"])
async def delete_order(id):
    return text("dummy")


@dummy.route("/products/<product_id>/orders/<order_id:int>", methods=["GET"])
async def get_product_order(product_id, order_id):
    return text("dummy")
