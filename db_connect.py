import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    # conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    return conn, cur

# from datetime import datetime
# conn, cur = get_db_connection()
# cur.arraysize = 10
# query = "INSERT INTO products (input_link, product_name, price) VALUES (?, ?, ?)"
# params = (str(datetime.now()),"itemName", "link")
# cur.execute(query, params)
# conn.commit()
# cur.execute("SELECT * FROM products")
# products = cur.fetchmany() 

# for product in products:
#     print (product)
#     print("------------------------")