from flask import Flask
from flask_cors import CORS, cross_origin


def create_app(config_obj):
    """создание экземляра flask приложения с нужным config'ом"""

    from tables.__all_models import Organisation, Post, Position, User, Review

    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_obj)

    from database import init_db

    init_db(app)

    return app
