import enum
import datetime

from sqlalchemy.orm import relationship

from app import db
from app.customer import Customer


class OrderStatusEnum(enum.Enum):
    feito = 'feito'
    pendente = 'pendente'
    concluido = 'concluido'


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.Enum(OrderStatusEnum))
    price = db.Column(db.Float())
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = relationship(Customer)
