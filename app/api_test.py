import pytest
import json

from app.test.fixtures import app, db

from app.api import app as api_app

from app.customer import CustomerService, CustomerSchema
from app.order import OrderService, OrderSchema

CUSTOMER_DATA = {
    'name': 'thomas',
    'last_name': 'hobbes',
    'email': 'test@test.com'
}

ORDER_DATA = {
    'status': 'concluido',
    'price': 20.0,
    'customer_id': 1
}


@pytest.fixture
def customer_schema():
    return CustomerSchema()


@pytest.fixture
def order_schema():
    return OrderSchema()


@pytest.fixture
def client():
    api_app.config['TESTING'] = True

    return api_app.test_client()


def test_get_customers(client, db, customer_schema):
    CustomerService.create(CUSTOMER_DATA)

    response = client.get('/clientes').get_json()

    CUSTOMER_DATA['id'] = 1
    assert customer_schema.load(response, many=True) == [CUSTOMER_DATA]


def test_get_orders(client, db):
    OrderService.create(ORDER_DATA)

    response = client.get('/pedidos').get_json()

    assert response[0]['status'] == ORDER_DATA['status']
    assert response[0]['preco'] == ORDER_DATA['price']
    assert response[0]['cliente_id'] == ORDER_DATA['customer_id']


def test_get_customer(client, db, customer_schema):
    CustomerService.create(CUSTOMER_DATA)

    response = client.get('/clientes/1').get_json()

    CUSTOMER_DATA['id'] = 1
    assert customer_schema.load(response) == CUSTOMER_DATA


def test_get_orders(client, db):
    OrderService.create(ORDER_DATA)

    response = client.get('/pedidos/1').get_json()

    assert response['status'] == ORDER_DATA['status']
    assert response['preco'] == ORDER_DATA['price']
    assert response['cliente_id'] == ORDER_DATA['customer_id']
