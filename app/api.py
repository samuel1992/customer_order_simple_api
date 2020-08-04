from flask import request

from app import create_app
from app.customer import Customer

app = create_app()


@app.route('/customers', methods=['POST', 'GET'])
def customers():
    if request.method == 'POST':
        import pdb;pdb.set_trace()

    customers = Customer.query.all()
    return f'{customers}'


@app.route('/orders')
def orders():
    pass
