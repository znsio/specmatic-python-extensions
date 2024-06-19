# Dummy Routes For Coverage Testing and Route-Adapter Testing
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

dummy = APIRouter()


@dummy.get("/orders/{id}")
def get_order(id):
    return PlainTextResponse("dummy")


@dummy.put("/orders/{id}")
def update_order(id):
    return PlainTextResponse("dummy")


@dummy.delete("/orders/{id}")
def delete_order(id):
    return PlainTextResponse("dummy")


@dummy.get("/products/{product_id}/orders/{order_id}")
def get_product_order(product_id, order_id):
    return PlainTextResponse("dummy")
