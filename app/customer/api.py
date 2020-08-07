from flask import request, Blueprint

from app.extensions import response

from .service import CustomerService
from .schema import customer_schema

app = Blueprint('customer_api', __name__)


@app.route('/clientes', methods=['GET'])
def customers_get():
    customers = CustomerService.get_all()
    return response(customer_schema.dump(customers, many=True), 200)


@app.route('/clientes', methods=['POST'])
def customers_post():
    customer_data = request.get_json()
    errors = customer_schema.validate(customer_data)
    if errors:
        return response({'errors': errors}, 400)

    customer = CustomerService.create(customer_schema.load(customer_data))
    return response(customer_schema.dump(customer), 201)


@app.route('/clientes/<int:customer_id>', methods=['GET'])
def customer_get(customer_id):
    customer = CustomerService.get_by_id(customer_id)
    return response(customer_schema.dump(customer), 200)


@app.route('/clientes/<int:customer_id>', methods=['PUT'])
def customer_put(customer_id):
    customer_data = request.get_json()
    errors = customer_schema.validate(customer_data)
    if errors:
        return response({'errors': errors}, 400)

    customer = CustomerService.update(customer_id,
                                      customer_schema.load(customer_data))
    return response(customer_schema.dump(customer), 200)


@app.route('/clientes/<int:customer_id>', methods=['DELETE'])
def customer_delete(customer_id):
    if CustomerService.delete(customer_id):
        return response({}, 204)

    return response({}, 404)
