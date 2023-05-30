import configparser
from sanic import Sanic

config = configparser.ConfigParser()
config.read('./../config.ini')

app = Sanic("OrderBFF")
app.config["ORDER_API_HOST"] = config.get('dev', 'ORDER_API_HOST')
app.config["ORDER_API_PORT"] = config.get('dev', 'ORDER_API_PORT')

from test.sanic_app.routes import *
