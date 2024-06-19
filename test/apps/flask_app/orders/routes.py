from flask import Blueprint, jsonify, request

from ..orders.models import Order
from ..services import OrdersService

orders = Blueprint("orders", __name__)


@orders.route("/orders", methods=["POST"])
def create_order():
    data: Order = Order.load(request.json)
    order = OrdersService.create_order(data)
    return jsonify(id=order["id"]), 201
