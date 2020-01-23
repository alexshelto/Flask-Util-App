

from flask import render_template, request, Blueprint, flash
from src import db
from src.model import graph_data

from datetime import datetime, date
# querying
import sqlite3
from sqlite3 import Error


db_path = "/Users/alexshelton/Desktop/Flask-Util-App/dev-env/src/data.sqlite"




def create_connection(db_path):
    _con = None #connection to db default val
    try:
        _con = sqlite3.connect(db_path)

    except Error as e:
        print("Error occured: {}".format(e))
    return _con


def returnTable(db_path):
    connection = create_connection(db_path)
    c = connection.cursor()
    c.execute("select * from graph_data order by id")
    table = c.fetchall()
    connection.close()
    return table

# change to return a desired weeks table
def returnWeeklyTable(db_path, weekNum):
    connection = create_connection(db_path)
    c = connection.cursor()
    ##Query
    SQL_WEEKLY_QUERY = """Select * from graph_data where week = ? order by day"""
    c.execute(SQL_WEEKLY_QUERY, (weekNum, ))
    weeklyTable = c.fetchall()
    connection.close()
    return weeklyTable

