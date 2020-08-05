from marshmallow import fields, Schema


class CustomerSchema(Schema):
    nome = fields.Str(attribute='name', required=True)
    ultimo_nome = fields.Str(attribute='last_name', required=True)
    email = fields.Str(required=True)

    class Meta:
        fields = ('id', 'nome', 'ultimo_nome', 'email')


customer_schema = CustomerSchema()
