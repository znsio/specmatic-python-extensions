# Dummy Routes For Coverage Testing and Route-Adapter Testing
from flask import Blueprint

dummy = Blueprint("dummy", __name__)


@dummy.route("/orders/<id>", methods=["GET"])
def get_order(id):
    return "dummy"


@dummy.route("/orders/<int:id>", methods=["PUT"])
def update_order(id):
    return "dummy"


@dummy.route("/orders/<int(min=1, signed=true):id>", methods=["DELETE"])
def delete_order(id):
    return "dummy"


@dummy.route("/products/<product_id>/orders/<int:order_id>", methods=["GET"])
def get_product_order(product_id, order_id):
    return "dummy"
