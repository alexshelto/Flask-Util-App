#Alexander Shelton
#Main content routing of webapp

from flask import render_template, request, Blueprint, flash
from src import db
from src.model import graph_data

from datetime import datetime


#Creating a blueprint instance
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    legend = 'Weekly Data'
    labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    values = [10,15,23,12,32,17,25]
    maxBar = max(values)
    return render_template('home.html', values=values, labels=labels, legend=legend, max=maxBar)


@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/data')
def data():
    return render_template('data.html')

@main.route('/<time>')
def enter(time):
    data = graph_data(time_spent=time)
    db.session.add(data)
    db.session.commit()
    return ('<h1> Added new info </h1>')



@main.route('/show')
def show():
    now = datetime.now()
    times = graph_data.query.filter_by(id=1)

    return render_template('test.html', times=times)
