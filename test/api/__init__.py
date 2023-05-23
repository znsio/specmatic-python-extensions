import os

from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config["ORDER_API_HOST"] = os.getenv("ORDER_API_PORT")
app.config["ORDER_API_PORT"] = os.getenv("ORDER_API_HOST")

from test.api.routes import *
