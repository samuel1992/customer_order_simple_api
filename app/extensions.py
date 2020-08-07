from flask import jsonify

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def response(data, status_code):
    return jsonify(data), status_code
