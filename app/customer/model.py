from app import db


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
