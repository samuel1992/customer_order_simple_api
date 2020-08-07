import pytest

from app.test.fixtures import app, db, client

from .schema import OrderSchema
from .service import OrderService
from .model import OrderStatusEnum


ORDER_DATA = {
    'status': OrderStatusEnum.novo,
    'price': 20.0,
    'customer_id': 1
}


@pytest.fixture
def order_schema():
    return OrderSchema()


def test_get_orders(client, db):
    OrderService.create(ORDER_DATA)

    response = client.get('/pedidos').get_json()

    assert response[0]['status'] == ORDER_DATA['status'].value
    assert response[0]['preco'] == ORDER_DATA['price']
    assert response[0]['cliente_id'] == ORDER_DATA['customer_id']


def test_get_order(client, db):
    OrderService.create(ORDER_DATA)

    response = client.get('/pedidos/1').get_json()

    assert response['status'] == ORDER_DATA['status'].value
    assert response['preco'] == ORDER_DATA['price']
    assert response['cliente_id'] == ORDER_DATA['customer_id']

def test_post_order(client, db, order_schema):
    data = order_schema.dump(ORDER_DATA)
    response = client.post('/pedidos', json=data)
    response_data = response.get_json()

    assert response.status_code == 201
    assert response_data['status'] == ORDER_DATA['status'].value
    assert response_data['preco'] == ORDER_DATA['price']
    assert response_data['cliente_id'] == ORDER_DATA['customer_id']


def test_post_order_with_error(client):
    data = {'wrong_field': 'wrong_value'}
    response = client.post('/pedidos', json=data)

    assert response.status_code == 400

def test_put_order(client, db, order_schema):
    OrderService.create(ORDER_DATA)

    new_status = 'entregue'
    data = {'status': new_status, 'preco': 20.0, 'cliente_id': 1}

    response = client.put("/pedidos/1", json=data)

    assert response.status_code == 200
    assert response.get_json()['status'] == new_status


def test_put_order_with_error(client):
    data = {'wrong_field': 'wrong_value'}
    response = client.put("/pedidos/1", json=data)

    assert response.status_code == 400


def test_delete_order(client, db):
    OrderService.create(ORDER_DATA)

    response = client.delete("/pedidos/1")

    assert response.status_code == 204


def test_delete_non_existent_order(client, db):
    OrderService.create(ORDER_DATA)

    response = client.delete("/pedidos/989898")

    assert response.status_code == 404
