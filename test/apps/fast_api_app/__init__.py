import configparser

from fastapi import FastAPI
from specmatic.utils import get_project_root

config = configparser.ConfigParser()
config.read(get_project_root() + '/test/config.ini')

app = FastAPI()
configuration = {"ORDER_API_HOST": config.get('dev', 'ORDER_API_HOST'),
                 "ORDER_API_PORT": config.get('dev', 'ORDER_API_PORT')}

from test.apps.fast_api_app.routes import *
