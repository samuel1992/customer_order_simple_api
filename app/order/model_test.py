from pytest import fixture

from app.customer import Customer
from app.test.fixtures import app, db

from .model import Order


@fixture
def customer():
    return Customer(name='arthur', last_name='schopenhauer',
                    email='test@test.com')


def test_order_create(db, customer):
    order = Order(price=20.0, customer_id=customer.id)
    db.session.add(order)
    db.session.commit()

    assert Order.query.first()
