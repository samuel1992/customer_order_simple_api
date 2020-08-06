from app.test.fixtures import client, app, db


def test_get_customers(client):
    response = client.get('/clientes')
