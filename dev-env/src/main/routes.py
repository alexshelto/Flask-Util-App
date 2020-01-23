#Alexander Shelton
#Main content routing of webapp

from flask import render_template, request, Blueprint, flash
from src import db
from src.model import graph_data

from datetime import datetime

# querying
import sqlite3
from sqlite3 import Error



#Creating a blueprint instance
main = Blueprint('main', __name__)



@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/<int:time>')
def enter(time):
    try: #converting num to string or chekcing if it is  astring. If it is not a string, value err, wont commit to db
        int_time = int(time)
        data = graph_data(time_spent=int_time)
        db.session.add(data)
        db.session.commit()
        return ('<h1> Added new info </h1>')

    except ValueError as e:
        print(e)
        return render_template("about.html")
