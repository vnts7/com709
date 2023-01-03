from datetime import datetime
import sqlite3
import os.path

# Absolute path for database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "charts.db")

db: sqlite3.Connection = None


def connect_db():
    """Create a connection to the sqlite database.

    Returns
    -------
    Connection
        a connection to the database
    """
    global db
    if not db:
        db = sqlite3.connect(db_path)
    return db


def close_db():
    """Close the connection to the sqlite database.
    """
    global db
    if db:
        db.close()
        db = None


def query(sql_query, param):
    """Connect to database and execute sql query

    Parameters
    ----------
    sql_query : string
        A valid sql query
    param : any
        A parameter to be passed in sql query

    Returns
    -------
    list
        a list of rows returned from the database by this query
    """
    # connect db and execute sql
    cur = connect_db().cursor()
    cur.execute(sql_query, (param,))
    rows = cur.fetchall()
    return rows

# Ensure that user enter a valid date


def input_date():
    """
    Require user to input a date until it is valid

    Returns
    -------
    datetime
        a valid date
    """
    date = None
    while (date == None):
        try:
            date_str = input('Date to look up (yyyy-mm-dd): ')
            date_list = date_str.split('-')
            date = datetime(int(date_list[0]), int(
                date_list[1]), int(date_list[2]))
        except:
            print("Please enter a valid date")
    return date


def input_year():
    """
    Require user to input a year until it is valid

    Returns
    -------
    int
        a valid year
    """
    year = None
    while (year == None):
        try:
            year = int(input('Year to look up (yyyy): '))
        except:
            print("Please enter a valid year")
    return year


def input_str(key):
    """
    Require user to input a string until it is not empty

    Parameters
    ----------
    key: string
        {key} to look up: 

    Returns
    -------
    string
        a not empty string
    """
    str = ''
    while (str == ''):
        try:
            str = input(f'{key} to look up: ')
        except:
            print(f"Please enter a valid {key}")
    return str
