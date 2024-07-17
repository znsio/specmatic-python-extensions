import json
import os
from datetime import UTC, datetime

from dotenv import load_dotenv
from flask import Flask, jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

load_dotenv()

app = Flask(__name__)
app.config["ORDER_API_HOST"] = os.getenv("ORDER_API_HOST")
app.config["ORDER_API_PORT"] = os.getenv("ORDER_API_PORT")
app.config["API_URL"] = (
    f"http://{app.config['ORDER_API_HOST']}:{app.config['ORDER_API_PORT']}"
)
app.config["AUTH_TOKEN"] = os.getenv("AUTH_TOKEN") or "API-TOKEN-SPEC"
app.config["REQ_TIMEOUT"] = os.getenv("REQ_TIMEOUT") or 3000


@app.errorhandler(ValidationError)
def handle_marshmallow_validation_error(e: "ValidationError"):
    return jsonify(
        timestamp=datetime.now(tz=UTC).isoformat(),
        status=400,
        error="Bad Request",
        message=json.dumps(e.messages),
    ), 400


@app.errorhandler(HTTPException)
def http_error_handler(e):
    return jsonify(
        timestamp=datetime.now(tz=UTC).isoformat(),
        status=e.code,
        error=e.name,
        message=e.description,
    ), e.code


from .dummy_routes import dummy  # noqa: E402
from .orders.routes import orders  # noqa: E402
from .products.routes import products  # noqa: E402

app.register_blueprint(products)
app.register_blueprint(orders)
app.register_blueprint(dummy)
