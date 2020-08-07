from flask import request, Blueprint

from app.extensions import response

from .service import CustomerService
from .schema import customer_schema

app = Blueprint('customer_api', __name__)


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
