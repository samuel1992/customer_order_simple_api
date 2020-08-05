from marshmallow import fields, Schema


class CustomerSchema(Schema):
    name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Str(required=True)

    class Meta:
        fields = ('id', 'name', 'last_name', 'email')


customer_schema = CustomerSchema()