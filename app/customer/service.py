from app.extensions import db

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

    @staticmethod
    def update(customer_id, customer_data):
        customer = Customer.query.get(customer_id)
        customer.query.update(customer_data)

        db.session.commit()

        return customer

    @staticmethod
    def delete(customer_id):
        customer = Customer.query.get(customer_id)
        if not customer:
            return []

        db.session.delete(customer)
        db.session.commit()

        return [customer_id]
