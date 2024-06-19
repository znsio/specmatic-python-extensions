from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..schemas import Order
from ..services import OrdersService

orders = APIRouter()


@orders.post("/orders")
async def create_order(order: Order):
    new_order = await OrdersService.create_order(order)
    return JSONResponse(status_code=201, content={"id": new_order["id"]})
