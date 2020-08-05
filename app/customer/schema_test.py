from pytest import fixture

from .model import Customer
from .schema import CustomerSchema


@fixture
def schema():
    return CustomerSchema()


def test_schema_create(schema):
    assert schema


def test_schema_serialization(schema):
    name = 'friedrich'
    last_name = 'nietzsche'
    email = 'test@test.com'
    customer_data = schema.load({
        'nome': name,
        'ultimo_nome': last_name,
        'email': email
    })

    customer = Customer(**customer_data)

    assert customer.name == name
    assert customer.last_name == last_name
    assert customer.email == email
