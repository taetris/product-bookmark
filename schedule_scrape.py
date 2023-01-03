from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

import time 
from scrape import scrape 
from db_connect import get_db_connection
from datetime import datetime

def connectDB_and_setSize():
    conn, cur = get_db_connection()
    cur.arraysize = 10
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
        # price =250
        # start_scheduler(db_link)

        update_at = str(datetime.now())

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

        # Define the UPDATE and INSERT queries
        update_query = "UPDATE products SET update_at=? WHERE input_link=?"
        insert_query = "INSERT INTO products (input_link, product_name, price, update_at) VALUES (?, ?, ?, ?)"

        # Define the parametrs for the queries
        update_params = (str(datetime.now()), link)
        insert_params = (link, itemName, price, str(datetime.now()))

        # Use the MySQL ON DUPLICATE KEY UPDATE syntax to execute either the UPDATE or INSERT query
        query = f"{update_query} ON CONFLICT {insert_query}"
        params = update_params + insert_params

        # Execute the query
        cur.execute(query, params)
        conn.commit()

        x=x+1
     
    print("----------------------")
    conn.close()
    
def schedd():
    print("scheduling...")
    scheduler = BackgroundScheduler(timezone = "Asia/Kathmandu")

    job = scheduler.add_job(myscheduler, 'interval', seconds = 20)
    scheduler.start()
    print(job, "done")



# start_scheduler()
# # Shut down the scheduler when you're done
# scheduler.shutdown()

# for link in linklist:
#     scheduler = BackgroundScheduler(timezone = "Asia/Kathmandu")
#     scheduler.start()

#     # job = scheduler.add_job(scrape, 'cron', [now], hour = "21", minute = "48")
#     # Running scrape() at interval of every hour
#     job = scheduler.add_job(scrape, 'interval', [link], seconds = 5)
#     print(job)

#     while True:
#         time.sleep(3)



# import threading
# import time

# def task1():
#     while True:
#         print("Task 1 is running")
#         time.sleep(2)

# def task2():
#     while True:
#         print("Task 2 is running")
#         time.sleep(3)

# thread1 = threading.Thread(target=task1)
# thread2 = threading.Thread(target=task2)

# thread1.start()
# thread2.start()