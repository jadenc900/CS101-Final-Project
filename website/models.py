from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import date

class Comments (db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(100000))
    # foreign Key link to class User 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#class Notifications(db.Model):
#    id = db.Column(db.Integer,primary_key=True)
#    data = db.Column(db.String(100000))
#    date = db.Column(db.Date.Time(timezone= True), default=func.now())
#    # foreign Key link to class User 
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50),unique = True)
    lname = db.Column(db.String(50),unique = True)
    netID = db.Column(db.String(6),unique = True)
    arrivaldate = db.Column(db.String(11))
    password = db.Column(db.String(20))
    notifications = db.relationship('Notification')
    comments = db.relationship("Comments")

