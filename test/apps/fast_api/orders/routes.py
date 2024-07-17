from fastapi import APIRouter

from ..schemas import Order
from ..services import OrdersService

orders = APIRouter()


@orders.post("/orders", status_code=201)
async def create_order(order: Order) -> dict[str, int]:
    new_order = await OrdersService.create_order(order)
    return {"id": new_order["id"]}
