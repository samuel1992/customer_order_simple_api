from marshmallow import fields, Schema
from marshmallow_enum import EnumField

from app.customer import CustomerSchema

from .model import OrderStatusEnum


class OrderSchema(Schema):
    data = fields.DateTime('%d-%m-%Y %H:%M:%S', attribute='date')
    status = EnumField(OrderStatusEnum, required=True)
    preco = fields.Float(attribute='price', required=True)
    cliente_id = fields.Integer(attribute='customer_id', required=True)
    cliente = fields.Nested(CustomerSchema, attribute='customer')

    class Meta:
        fields = ('id', 'data', 'status', 'preco', 'cliente', 'cliente_id')


order_schema = OrderSchema()
