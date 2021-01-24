from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Company(db.Model):
    __tablename__ = 'Company'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    phone = db.Column(db.Integer())
    address = db.Column(db.String())

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
