# Alex Shelton
# Routes.py : handles all routing that has to do with showing/manipulating data
# For files that show graphing OR tableview or sql data
#


from flask import render_template, request, Blueprint, flash, redirect
from src import db
from src.model import graph_data

from datetime import datetime, date
# querying
import sqlite3
from sqlite3 import Error
from src.data import dbtools



db_path = "/Users/alexshelton/Desktop/Flask-Util-App/dev-env/src/data.sqlite"



#Creating a blueprint instance
data = Blueprint('data', __name__)

@data.route('/tableview',methods=['GET', 'POST'])
def tableview():
    THISWEEK = date.today().isocalendar()[1] #Number of the current week number ex: jan 1st would return '1'

    if request.method == 'POST':
        selected_week =  int(request.form.get('week'))
        #Checking bounds weeks are 1-52:
        if selected_week > 52 or selected_week < 0:
            flash("invalid")
            pass# Leave if statement logic: show current weeks table
        
        #IF week is 0: web page loads whole table
        elif selected_week == 0:
            alldata = dbtools.returnTable(db_path)
            return render_template('tableview.html', data=alldata, week=THISWEEK)
        
        #else load week:
        else:
            weekdata = dbtools.returnWeeklyTable(db_path, selected_week)
            return render_template('tableview.html', data=weekdata, week=THISWEEK)

    #Code executes if inputted week was > 52 or < 0:
    current_week = dbtools.returnWeeklyTable(db_path, THISWEEK)
    return render_template('tableview.html', data=current_week, week=THISWEEK)





@data.route('/weekdata')
def weekdata():
    # grab current week number
    # returnWeeklySums returns an array with totals for mon-fri. size n = 7

    THISWEEK = date.today().isocalendar()[1] #Number of the current week number ex: jan 1st would return '1'
    weekly_data = dbtools.returnWeeklySums(db_path,THISWEEK)
    legend = 'Weekly Data'
    labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render_template('weekdata.html', values=weekly_data, labels=labels, legend=legend)




@data.route('/summary_data')
def summary_data():
    # grab current week number
    # returnWeeklySums returns an array with totals for mon-fri. size n = 7
    # return n = 52 size array with sums of every week
    
    THISWEEK = date.today().isocalendar()[1] #Number of the current week number ex: jan 1st would return '1'
    LASTWEEK = THISWEEK -1
    weekly_data = dbtools.returnWeeklySums(db_path,LASTWEEK)
    all_weeks_data = dbtools.return52weeks(db_path)
    labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render_template('summary_data.html', labels= labels, values=weekly_data, plot_data = all_weeks_data)
