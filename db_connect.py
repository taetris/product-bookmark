import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    # conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    return conn, cur