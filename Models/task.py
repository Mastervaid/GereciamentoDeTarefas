from flask_sqlalchemy import SQLAlchemy
from . import db

#create model Task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100) )
    date = db.Column(db.String(10))
    status = db.Column(db.String(20))


