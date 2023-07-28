from typing import List

from fastapi import HTTPException
from fastapi.params import Query

from test.apps.fast_api_app import app
from test.apps.fast_api_app.products import Products

import json as jsonp


@app.get("/findAvailableProducts", response_model=List[dict])
def find_available_products(type: str = Query(None, description="Filter by product type")):
    if not type:
        raise HTTPException(status_code=400, detail="Missing 'type' query parameter")
    response = Products().search(type)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="An error occurred while retrieving the products")

    product_list = jsonp.loads(response.content)

    products = [
        {"id": product["id"], "name": product["name"], "type": product["type"], "inventory": product["inventory"]} for
        product in product_list]
    return products
