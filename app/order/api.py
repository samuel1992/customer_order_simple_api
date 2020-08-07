from flask import request, Blueprint

from app.extensions import response

from .schema import order_schema
from .service import OrderService

app = Blueprint('order_api', __name__)


@app.route('/pedidos', methods=['GET', 'POST'])
def orders():
    if request.method == 'POST':
        order_data = request.get_json()
        errors = order_schema.validate(order_data)
        if errors:
            return response({'errors': errors}, 400)

        order = OrderService.create(order_schema.load(order_data))
        return response(order_schema.dump(order), 201)

    orders = OrderService.get_all()
    return response(order_schema.dump(orders, many=True), 200)


@app.route('/pedidos/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def order(order_id):
    if request.method == 'PUT':
        order_data = request.get_json()
        errors = order_schema.validate(order_data)
        if errors:
            return response({'errors': errors}, 400)

        order = OrderService.update(order_id, order_schema.load(order_data))
        return response(order_schema.dump(order), 200)

    if request.method == 'DELETE':
        if OrderService.delete(order_id):
            return response({}, 204)
        else:
            return response({}, 404)

    order = OrderService.get_by_id(order_id)
    return response(order_schema.dump(order), 200)
