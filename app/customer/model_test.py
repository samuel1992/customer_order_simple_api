from app.test.fixtures import app, db

from .model import Customer


def test_customer_create(db):
    customer = Customer(name='arthur', last_name='schopenhauer',
                        email='test@test.com')
    db.session.add(customer)
    db.session.commit()

    assert Customer.query.first()
