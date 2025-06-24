from server.config import db

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    occupation = db.Column(db.String(120), nullable=True)

    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')
