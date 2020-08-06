import pytest

from app.test.fixtures import app, db

from .model import Customer
from .service import CustomerService

CUSTOMER_DATA = {
    'name': 'thomas',
    'last_name': 'hobbes',
    'email': 'test@test.com'
}


def test_create(db):
    customer = CustomerService.create(CUSTOMER_DATA)

    for key in CUSTOMER_DATA.keys():
        assert getattr(customer, key) == CUSTOMER_DATA[key]


def test_get_all(db):
    CustomerService.create(CUSTOMER_DATA)
    customers = CustomerService.get_all()

    assert len(customers) == 1


def test_get_by_id(db):
    customer = CustomerService.create(CUSTOMER_DATA)

    assert CustomerService.get_by_id(1) == customer


def test_update(db):
    customer = CustomerService.create(CUSTOMER_DATA)
    new_name = 'Rousseau'
    updated_customer = CustomerService.update(customer.id, {'name': new_name})

    assert customer.name == new_name
    assert updated_customer == customer


def test_delete(db):
    customer = CustomerService.create(CUSTOMER_DATA)

    deleted_ids = CustomerService.delete(customer.id)

    assert len(Customer.query.all()) == 0
    assert deleted_ids[0] == customer.id


def teste_empty_delete(db):
    deleted_ids = CustomerService.delete(42)

    assert deleted_ids == []
