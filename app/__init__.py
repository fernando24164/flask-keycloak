import logging

from flask import Flask
from .config import config_by_name
from app.api import api_final


logging.basicConfig(level=logging.DEBUG)


def create_app(config_name="dev"):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    api_final.init_app(app)

    return app
