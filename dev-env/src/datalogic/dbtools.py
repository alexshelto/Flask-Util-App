


from datetime import date, time
import sqlite3
from sqlite3 import Error
import random

db_path = "/Users/alexshelton/Desktop/Flask-Util-App/dev-env/src/data.sqlite"



'''
ID  | week | Day | time spent | timestamp
------------------------------------------
    |      |     |            |
'''

def create_connection(db_path):
    _con = None #connection to db default val
    try:
        _con = sqlite3.connect(db_path)

    except Error as e:
        print("Error occured: {}".format(e))
    return _con

def return_table(cursor, db_name):
    cursor.execute(str("select * from ")+db_name)
    entire = cursor.fetchall()

    return entire


def main():
    connection = create_connection(db_path)
    cursor = connection.cursor()


    cursor.execute("select * from graph_data order by day")
    weekly = cursor.fetchall() #tuple

    ## Replacing any facivon io value
    print("ID  | week | Day | time spent | timestamp")
    for row in weekly:
        if row[3] == 'show': #time spent is 3rd
            row_id = row[0]
            print(row_id)
            num = random.randint(0,10)
            cursor.execute('UPDATE graph_data SET time_spent=? WHERE ID=?',(num,row_id))
            connection.commit()


    #
    # entire = return_table(cursor, "graph_data")
    # for row in entire:
    #     print(row)
    #









    connection.close()
    print("Closed Connection") #Debugging









if __name__ == '__main__':
    main()
