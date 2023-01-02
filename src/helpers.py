import sqlite3
import os.path

#Absolute path for database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "charts.db")

db: sqlite3.Connection = None

def connect_db():
    """Create a connection to the sqlite database.
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

