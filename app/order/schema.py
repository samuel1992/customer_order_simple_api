from marshmallow import fields, Schema

from app.customer import CustomerSchema


class OrderSchema(Schema):
    data = fields.Str(attribute='date', required=True)
    status = fields.Str(required=True)
    preco = fields.Str(attribute='price', required=True)
    customer = fields.Nested(CustomerSchema)


order_schema = OrderSchema()
