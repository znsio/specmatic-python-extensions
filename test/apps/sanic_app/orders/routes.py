from typing import TYPE_CHECKING

from sanic import Blueprint, json

from ..orders.models import Order
from ..services import OrdersService

if TYPE_CHECKING:
    from sanic import Request

orders = Blueprint("orders")


@orders.route("/orders", methods=["POST"])
async def create_order(request: "Request"):
    data: Order = Order.load(request.json)
    order = OrdersService.create_order(data)
    return json({"id": order["id"]}, status=201)
