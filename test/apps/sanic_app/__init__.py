import os
import json as jsonlib
from datetime import UTC, datetime

from dotenv import load_dotenv
from marshmallow import ValidationError
from sanic import Sanic, json
from sanic.exceptions import SanicException

load_dotenv()
app = Sanic("OrderBFF")
app.config["ORDER_API_HOST"] = os.getenv("ORDER_API_HOST")
app.config["ORDER_API_PORT"] = os.getenv("ORDER_API_PORT")
app.config["API_URL"] = (
    f"http://{app.config['ORDER_API_HOST']}:{app.config['ORDER_API_PORT']}"
)
app.config["AUTH_TOKEN"] = os.getenv("AUTH_TOKEN") or "API-TOKEN-SPEC"
app.config["REQ_TIMEOUT"] = os.getenv("REQ_TIMEOUT") or 3000


@app.exception(ValidationError)
async def handle_marshmallow_validation_error(_, exc: "ValidationError"):
    # NOTE:API SPEC V4 specifies that message should be a string not an object / array
    return json(
        {
            "timestamp": datetime.now(tz=UTC).isoformat(),
            "status": 400,
            "error": "Bad Request",
            "message": jsonlib.dumps(exc.messages),
        },
        status=400,
    )


@app.exception(SanicException)
async def http_error_handler(_, exception: "SanicException"):
    return json(
        {
            "timestamp": datetime.now(tz=UTC).isoformat(),
            "status": exception.status_code,
            "error": exception.__class__.__name__,
            "message": str(exception),
        },
        status=exception.status_code,
    )


from .dummy_routes import dummy  # noqa: E402
from .orders.routes import orders  # noqa: E402
from .products.routes import products  # noqa: E402

app.blueprint(products)
app.blueprint(orders)
app.blueprint(dummy)
