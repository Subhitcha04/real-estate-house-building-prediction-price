import sqlite3 as sq
import pandas as pd

def connect_db(filename):
    connection = sq.connect('information.db')
    curs = connection.cursor()
    curs.execute("create table if not exists realEstate" +
             " (price integer, area integer, bedroom integer, bathroom integer, stories integer, mainroad integer,guestroom integer,basement integer, hotwaterheating integer, airconditioning integer, parking integer, prefarea integer, furnishingstatus text)")
    database= pd.read_csv(filename)
 
    # Write the data to a sqlite db table
    database.to_sql('userInfo', connection, if_exists='replace', index=False)

    # Run select sql query
    curs.execute('select * from userInfo')

    # Fetch all records
    # as list of tuples
    records = curs.fetchall()

    # Display result 
    for row in records:
    # show row
        print(row)

    # Close connection to SQLite database
    connection.close()
