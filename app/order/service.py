from app.extensions import db

from .model import Order


class OrderService:
    @staticmethod
    def create(params):
        new_order = Order(**params)

        db.session.add(new_order)
        db.session.commit()

        return new_order

    @staticmethod
    def get_all():
        return Order.query.all()

    @staticmethod
    def get_by_id(order_id):
        return Order.query.get(order_id)

    @staticmethod
    def update(order_id, order_data):
        order = Order.query.get(order_id)
        order.query.update(order_data)

        db.session.commit()

        return order

    @staticmethod
    def delete(order_id):
        order = Order.query.get(order_id)
        if not order:
            return []

        db.session.delete(order)
        db.session.commit()

        return [order_id]
