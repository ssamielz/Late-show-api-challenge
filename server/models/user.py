from __init__ import db, SerializerMixin

class User(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer primary_key=True)
    username = db.Column(db.String)
    password_hash = db.Column(db.String)


