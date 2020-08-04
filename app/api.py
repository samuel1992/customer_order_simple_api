from flask import request

from app import create_app
from app.customer import (Customer, CustomerService, customer_schema,
                          customers_schema)

app = create_app()


@app.route('/customers', methods=['POST', 'GET'])
def customers():
    if request.method == 'POST':
        customer_data = request.get_json()
        errors = customer_schema.validate(customer_data)
        if errors:
            return {'errors': errors}

        return customer_schema.dump(CustomerService.create(customer_data))

    return customers_schema.dump(Customer.query.all())


@app.route('/orders')
def orders():
    pass
