from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

import time 
from scrape import scrape 
from db_connect import get_db_connection


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
        itemName, price = scrape(link)
        # start_scheduler(link)
        query = "UPDATE products SET price=?, product_name=? WHERE input_link=?"
        params = (price, itemName, link)
        cur.execute(query, params)
        conn.commit()
        x=x+1
    
    print("----------------------")
    conn.close()
    
def schedd():
    print("scheduling...")
    scheduler = BackgroundScheduler(timezone = "Asia/Kathmandu")

    job = scheduler.add_job(myscheduler, 'interval', seconds = 60)
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