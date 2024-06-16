from datetime import UTC, datetime

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

load_dotenv()
app = FastAPI()


@app.exception_handler(RequestValidationError)
def handle_marshmallow_validation_error(_, e: "RequestValidationError"):
    return JSONResponse(
        status_code=400,
        content={
            "timestamp": datetime.now(tz=UTC).isoformat(),
            "status": 400,
            "error": "Bad Request",
            "message": str(e),
        },
    )


@app.exception_handler(HTTPException)
def http_error_handler(_, e: "HTTPException"):
    return JSONResponse(
        status_code=e.status_code,
        content={
            "timestamp": datetime.now(tz=UTC).isoformat(),
            "status": e.status_code,
            "error": e.__class__.__name__,
            "message": e.detail,
        },
    )


from .dummy_routes import dummy  # noqa: E402
from .orders.routes import orders  # noqa: E402
from .products.routes import products  # noqa: E402

app.include_router(products)
app.include_router(orders)
app.include_router(dummy)