import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO products (item_name, first_scrape, first_price) VALUES (?, ?, ?)",
            ('First Product', 'Time', 'Content for the first post')
            )


connection.commit()
connection.close()