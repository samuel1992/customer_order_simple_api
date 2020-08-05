from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.config import DevelopmentConfig, TestingConfig

db = SQLAlchemy()


def create_app(testing=False):
    app = Flask(__name__)

    if testing:
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    return app
