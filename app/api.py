from flask import request, jsonify

from app import create_app
from app.customer import CustomerService, customer_schema
from app.order import OrderService, order_schema

app = create_app()


def response(data, status_code):
    return jsonify(data), status_code


@app.route('/clientes', methods=['POST', 'GET'])
def customers():
    if request.method == 'POST':
        customer_data = request.get_json()
        errors = customer_schema.validate(customer_data)
        if errors:
            return response({'errors': errors}, 400)

        customer = CustomerService.create(customer_schema.load(customer_data))
        return response(customer_schema.dump(customer), 201)

    customers = CustomerService.get_all()
    return response(customer_schema.dump(customers, many=True), 200)


@app.route('/clientes/<int:customer_id>', methods=['GET', 'PUT', 'DELETE'])
def customer(customer_id):
    if request.method == 'PUT':
        customer_data = request.get_json()
        errors = customer_schema.validate(customer_data)
        if errors:
            return response({'errors': errors}, 400)

        customer = CustomerService.update(customer_id,
                                          customer_schema.load(customer_data))
        return response(customer_schema.dump(customer), 200)

    if request.method == 'DELETE':
        if CustomerService.delete(customer_id):
            return response({}, 204)
        else:
            return response({}, 404)

    customer = CustomerService.get_by_id(customer_id)
    return response(customer_schema.dump(customer), 200)


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
