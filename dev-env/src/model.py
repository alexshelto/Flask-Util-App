#Alexander Shelton
#Database for weekly raspberry pi time data
#







from flask import current_app
from src import db #importing the db instance created in src/__init__.py

from datetime import datetime #used for date_created



class graph_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # week = db.Column(db.Integer, nullable=False)
    # day = db.Column(db.Integer, nullable=False)
    time_spent = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
