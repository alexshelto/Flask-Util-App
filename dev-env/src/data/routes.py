
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
    # TODO: FIX long query code in db tools function
    #
    #
    #
    THISWEEK = date.today().isocalendar()[1] #Number of the current week number ex: jan 1st would return '1'
    weeklyData = [0]*7
    dataDate = 0

    weeklyTable = dbtools.returnWeeklyTable(db_path, THISWEEK)
    for row in weeklyTable:
        if row[1] != dataDate:
            totalTime = 0
            dataDate = row[2]
        weeklyData[dataDate] += row[3] #adding total

    legend = 'Weekly Data'
    labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render_template('weekdata.html', values=weeklyData, labels=labels, legend=legend)




@data.route('/summary_data')
def summary_data():
    THISWEEK = date.today().isocalendar()[1] #Number of the current week number ex: jan 1st would return '1'
    #check for week not being '1' or will display last years set
    LASTWEEK = THISWEEK-1
    last_week = dbtools.returnWeeklyTable(db_path, LASTWEEK)


    return render_template('summary_data.html', data=last_week)
