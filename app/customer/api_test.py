import pytest
import json

from app.test.fixtures import app, db, client

from .service import CustomerService
from .schema import CustomerSchema

CUSTOMER_DATA = {
    'name': 'thomas',
    'last_name': 'hobbes',
    'email': 'test@test.com'
}


@pytest.fixture
def customer_schema():
    return CustomerSchema()


def test_get_customers(client, db, customer_schema):
    CustomerService.create(CUSTOMER_DATA)

    response = client.get('/clientes').get_json()

    CUSTOMER_DATA['id'] = 1
    assert customer_schema.load(response, many=True) == [CUSTOMER_DATA]


def test_get_customer(client, db, customer_schema):
    CustomerService.create(CUSTOMER_DATA)

    response = client.get('/clientes/1').get_json()

    CUSTOMER_DATA['id'] = 1
    assert customer_schema.load(response) == CUSTOMER_DATA


def test_post_customer(client, db, customer_schema):
    data = customer_schema.dump(CUSTOMER_DATA)
    response = client.post('/clientes', json=data)

    assert response.status_code == 201
    assert response.get_json() == data


def test_post_customer_with_error(client):
    data = {'wrong_field': 'wrong_value'}
    response = client.post('/clientes', json=data)

    assert response.status_code == 400

def test_put_customer(client, db, customer_schema):
    CustomerService.create(CUSTOMER_DATA)

    new_name = 'Foucault'
    CUSTOMER_DATA['name'] = new_name
    data = customer_schema.dump(CUSTOMER_DATA)

    response = client.put(f"/clientes/{CUSTOMER_DATA['id']}", json=data)

    assert response.status_code == 200
    assert response.get_json()['nome'] == new_name


def test_put_customer_with_error(client):
    data = {'wrong_field': 'wrong_value'}
    response = client.put(f"/clientes/{CUSTOMER_DATA['id']}", json=data)

    assert response.status_code == 400


def test_delete_customer(client, db):
    CustomerService.create(CUSTOMER_DATA)

    response = client.delete(f"/clientes/{CUSTOMER_DATA['id']}")

    assert response.status_code == 204


def test_delete_non_existent_customer(client, db):
    CustomerService.create(CUSTOMER_DATA)

    response = client.delete("/clientes/989898")

    assert response.status_code == 404
