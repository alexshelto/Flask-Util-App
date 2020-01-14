#Alexander Shelton
#Database for weekly raspberry pi time data
#







from flask import current_app
from src import db #importing the db instance created in src/__init__.py

from datetime import datetime, date #used for week#, day#, & timestamp: date_created

import sqlite3
from sqlite3 import Error


# TODO: Add year: (datetime.today().year)




'''
ID  | week | Day | time spent | timestamp
------------------------------------------
    |      |     |            |
'''
class graph_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer, default=date.today().isocalendar()[1]) #week number of the year. 1-52
    day = db.Column(db.Integer, default=datetime.today().weekday()) #day of the week, 0:monday, 6: sunday
    time_spent = db.Column(db.Integer, nullable=False, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)
