from flask import Flask, Blueprint

from app.config import DevelopmentConfig, TestingConfig
from app.customer import app as customer_blueprint
from app.order import app as order_blueprint

from .extensions import db


def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    app.register_blueprint(customer_blueprint)
    app.register_blueprint(order_blueprint)

    db.init_app(app)

    return app
