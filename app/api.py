from flask import request, jsonify

from app import create_app
from app.customer import CustomerService, customer_schema

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

        return response(
            customer_schema.dump(CustomerService.create(customer_data)),
            201
        )

    return response(
        customer_schema.dump(CustomerService.get_all(), many=True),
        200
    )


@app.route('/clientes/<int:customer_id>', methods=['GET', 'PUT', 'DELETE'])
def customer(customer_id):
    if request.method == 'PUT':
        customer_data = request.get_json()
        errors = customer_schema.validate(customer_data)
        if errors:
            return response({'errors': errors}, 400)

        return response(
            customer_schema.dump(CustomerService.update(customer_id,
                                                        customer_data)),
            200
        )

    if request.method == 'DELETE':
        if CustomerService.delete_by_id(customer_id):
            return response({}, 204)
        else:
            return response({}, 404)

    return response(
        customer_schema.dump(CustomerService.get_by_id(customer_id)),
        200
    )
