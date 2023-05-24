import os

from sanic import Sanic
from dotenv import load_dotenv

load_dotenv()
app = Sanic("OrderBFF")
app.config["ORDER_API_HOST"] = os.getenv("ORDER_API_HOST")
app.config["ORDER_API_PORT"] = os.getenv("ORDER_API_PORT")

from test.sanic_app.routes import *
