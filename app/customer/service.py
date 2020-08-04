from app import db

from .model import Customer


class CustomerService:
    @staticmethod
    def create(params):
        new_customer = Customer(**params)

        db.session.add(new_customer)
        db.session.commit()

        return new_customer

    @staticmethod
    def get_all():
        return Customer.query.all()

    @staticmethod
    def get_by_id(customer_id):
        return Customer.query.get(customer_id)
