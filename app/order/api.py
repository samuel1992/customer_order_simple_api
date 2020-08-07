from flask import request, Blueprint

from app.extensions import response

from .schema import order_schema
from .service import OrderService

app = Blueprint('order_api', __name__)


@app.route('/pedidos', methods=['GET'])
def orders_get():
    orders = OrderService.get_all()
    return response(order_schema.dump(orders, many=True), 200)


@app.route('/pedidos', methods=['POST'])
def orders_post():
    order_data = request.get_json()
    errors = order_schema.validate(order_data)
    if errors:
        return response({'errors': errors}, 400)

    order = OrderService.create(order_schema.load(order_data))
    return response(order_schema.dump(order), 201)


@app.route('/pedidos/<int:order_id>', methods=['GET'])
def order_get(order_id):
    order = OrderService.get_by_id(order_id)
    return response(order_schema.dump(order), 200)


@app.route('/pedidos/<int:order_id>', methods=['PUT'])
def order_put(order_id):
    order_data = request.get_json()
    errors = order_schema.validate(order_data)
    if errors:
        return response({'errors': errors}, 400)

    order = OrderService.update(order_id, order_schema.load(order_data))
    return response(order_schema.dump(order), 200)


@app.route('/pedidos/<int:order_id>', methods=['DELETE'])
def order_delete(order_id):
    if OrderService.delete(order_id):
        return response({}, 204)

    return response({}, 404)
