from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model,UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))
    name=db.Column(db.String(100))
    events=db.relationship('Event')

class Event(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    event=db.Column(db.String(1000))
    date = db.Column(db.Date)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    