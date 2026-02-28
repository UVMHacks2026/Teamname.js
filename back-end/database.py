import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "app.db")

# Returns an SQLite3 connection
def get_connection():

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection

# Initializes the database using the schema file
def init_db():
    connection = get_connection()

    schema_path = os.path.join(BASE_DIR, "schema.sql")

    with open(schema_path, "r") as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()