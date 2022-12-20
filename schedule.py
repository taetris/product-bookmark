from apscheduler.schedulers.background import BackgroundScheduler
import time 
from scrape import scrape 
from db_connect import get_db_connection

def tuple_to_list(links):
    linklist =[]
    for link in links:
        linklist.append(link[0])
    return linklist

def connectDB_and_setSize():
    conn, cur = get_db_connection()
    cur.arraysize = 4
    cur.execute("SELECT * FROM products")
    return conn, cur

def myscheduler():
    print("hello")
    conn, cur = connectDB_and_setSize()
    while True:
        links = cur.fetchmany() 
        # if not links:
        #     break
        linklist = tuple_to_list(links)

        for link in linklist:
            itemName, price = scrape(link)
            # start_scheduler(link)
            query = "UPDATE products SET price=?, product_name=? WHERE input_link=?"
            # query = "UPDATE products SET price = {0}, product_name = {1} WHERE input_link = '{2}'".format(price, itemName, link)
            params = (price, itemName, link)
            cur.execute(query, params)
            conn.commit()
            time.sleep(1)
        time.sleep(1)
    conn.close()
    
def hello():
    print("hiiiiiii")
    
def start_scheduler():
    scheduler = BackgroundScheduler(timezone = "Asia/Kathmandu")
    scheduler.start()
    link = "https://www.sastodeal.com/lnspirion-15-gaming-series-g5-i7-11800h-16gb-8x2-512gb-15-6-120hz-250nits-r-sd-dlpts-033.html"

    job = scheduler.add_job(scrape, 'interval',[link], seconds = 5)
    
    # scheduler.add_listener(out, event='job_success', job_id='my_job_id')

start_scheduler()


# query = "UPDATE products SET price = {0} WHERE name = '{1}'".format(new_price, product_name)
# cursor.execute(query)
# connection.commit()
# cursor.close()
# connection.close()


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