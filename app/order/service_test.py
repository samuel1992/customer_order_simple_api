import pytest

from app.test.fixtures import app, db

from .model import Order, OrderStatusEnum
from .service import OrderService

ORDER_DATA = {
    'status': OrderStatusEnum.entregue,
    'price': 20.0,
    'customer_id': 1
}


def test_create(db):
    order = OrderService.create(ORDER_DATA)

    for key in ORDER_DATA.keys():
        assert getattr(order, key) == ORDER_DATA[key]


def test_get_all(db):
    OrderService.create(ORDER_DATA)
    orders = OrderService.get_all()

    assert len(orders) == 1


def test_get_by_id(db):
    order = OrderService.create(ORDER_DATA)

    assert OrderService.get_by_id(1) == order


def test_update(db):
    order = OrderService.create(ORDER_DATA)
    new_status = OrderStatusEnum.novo
    updated_order = OrderService.update(order.id, {'status': new_status})

    assert order.status == new_status
    assert updated_order == order


def test_delete(db):
    order = OrderService.create(ORDER_DATA)

    deleted_ids = OrderService.delete(order.id)

    assert len(Order.query.all()) == 0
    assert deleted_ids[0] == order.id


def teste_empty_delete(db):
    deleted_ids = OrderService.delete(42)

    assert deleted_ids == []
