from pytest import fixture

from .model import Order, OrderStatusEnum
from .schema import OrderSchema

from app.customer import CustomerSchema


@fixture
def customer_schema():
    return CustomerSchema()


@fixture
def order_schema():
    return OrderSchema()


def test_schema_create():
    assert order_schema


def test_schema_serialization(order_schema, customer_schema):
    status = OrderStatusEnum.feito
    price = 20.0
    customer_data = {'nome': 'test', 'ultimo_nome': 'test',
                     'email': 'test@teste.com'}

    order_data = order_schema.load({
        'data': '27-10-2020 00:00:00',
        'status': status.value,
        'preco': price,
        'cliente': customer_data,
        'cliente_id': 1
    })

    order = Order(**order_data)

    assert order.status == status
    assert order.price == price
    assert order.customer == customer_schema.load(customer_data)
