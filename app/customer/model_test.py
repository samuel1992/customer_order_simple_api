from pytest import fixture

from .model import Customer


@fixture
def customer():
    return Customer(name='arthur', last_name='schopenhauer',
                    email='test@test.com')


def test_customer_create(customer):
    assert customer
