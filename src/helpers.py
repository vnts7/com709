import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "charts.db")

db: sqlite3.Connection = None


def connect_db():
    global db
    if not db:
        db = sqlite3.connect(db_path)
    return db


def close_db():
    global db
    if db:
        db.close()
        db = None

