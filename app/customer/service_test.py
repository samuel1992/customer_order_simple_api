from flask_sqlalchemy import SQLAlchemy

from app.test.fixtures import app, db

from .model import Customer
from .service import CustomerService


def test_create(db):
    customer_data = {
        'name': 'thomas',
        'last_name': 'hobbes',
        'email': 'test@test.com'
    }

    CustomerService.create(customer_data)
    customers = Customer.query.all()

    assert len(customers) == 1

    #for key in customer_data.keys():
    #    assert getattr(customers[0], key) == customer_data[key]

