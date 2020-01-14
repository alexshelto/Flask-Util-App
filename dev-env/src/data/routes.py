
from flask import render_template, request, Blueprint, flash
from src import db
from src.model import graph_data


from datetime import datetime
# querying
import sqlite3
from sqlite3 import Error



db_path = "/Users/alexshelton/Desktop/Flask-Util-App/dev-env/src/data.sqlite"


#Creating a blueprint instance
data = Blueprint('data', __name__)




def create_connection(db_path):
    _con = None #connection to db default val
    try:
        _con = sqlite3.connect(db_path)

    except Error as e:
        print("Error occured: {}".format(e))
    return _con


# def return_table(cursor, db_name):
#     cursor.execute(str("select * from ")+db_name)
#     entire = cursor.fetchall()
#     return entire





@data.route('/tableview', defaults={'week_num':None})
@data.route('/tableview/<int:week_num>')
def tableview(week_num):
    connection = create_connection(db_path)
    cursor = connection.cursor()
    cursor.execute("select * from graph_data order by id")
    all_view = cursor.fetchall()
    connection.close()

    if week_num == None or week_num > 52:
        return render_template('tableview.html', data=all_view)
    else:
        week_data = []
        for row in all_view:
            if row[1] == week_num:
                week_data.append(row)

        week = tuple(week_data)
        return render_template('tableview.html', data=week)




@data.route('/weekdata')
def weekdata():
    legend = 'Weekly Data'
    labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    values = [10,15,23,12,32,17,25]
    return render_template('weekdata.html', values=values, labels=labels, legend=legend)




@data.route('/summary_data')
def summary_data():
    return render_template('summary_data.html')
