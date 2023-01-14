from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

import time 
from scrape import scrape 
from db_connect import get_db_connection
from datetime import datetime

def connectDB_and_setSize():
    conn, cur = get_db_connection()
    cur.arraysize = 20
    cur.execute("SELECT * FROM products")
    return conn, cur

def myscheduler():
    x = 1
    conn, cur = connectDB_and_setSize()
    products = cur.fetchmany() 
    
    for product in products:
        print("loop: ", x)
        link = product[0]
        db_price = product[2]
        itemName, price = scrape(link)
        # price =150
        # start_scheduler(db_link)

        update_at = str(datetime.now())

        
        # Define the UPDATE and INSERT queries
        update_query = " UPDATE SET update_at=? WHERE input_link=?"
        insert_query = "INSERT INTO products (input_link, product_name, price, update_at) VALUES (?, ?, ?, ?)"

        # Define the parametrs for the queries
        update_params = (str(datetime.now()), link)
        insert_params = (link, itemName, price, str(datetime.now()))

        # Use the MySQL ON DUPLICATE KEY UPDATE syntax to execute either the UPDATE or INSERT query
        query = f"{insert_query} ON CONFLICT DO {update_query}"
        params = (*insert_params, *update_params)


        # Execute the query
        cur.execute(query, params)
        conn.commit()

        x=x+1
     
    print("----------------------")
    conn.close()

    if (price < db_price):
        print("prices dropped")
        send_mail()
    
def schedd():
    print("scheduling...")
    scheduler = BackgroundScheduler(timezone = "Asia/Kathmandu")

    job = scheduler.add_job(myscheduler, 'interval', seconds = 40)
    scheduler.start()
    print(job, "done")


# params = (link, itemName, price,update_at, update_at)
        
        # cur.execute("INSERT INTO products (input_link, product_name, price, update_at) VALUES (?, ?, ?, ?) ON CONFLICT(input_link,price) 
        # DO UPDATE products SET update_at=?", params)
        # conn.commit()

        # if (db_price == price):
        #     query = "UPDATE products SET update_at=? WHERE input_link=?"
        #     update_at = str(datetime.now())
        #     params = (update_at, link)
        # else:
            # query = "INSERT INTO products (input_link, product_name, price, update_at) VALUES (?, ?, ?, ?)"
        #     params = (link, itemName, price, update_at)
        
        # cur.execute(query, params)
        # conn.commit()
