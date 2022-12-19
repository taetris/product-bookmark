from apscheduler.schedulers.background import BackgroundScheduler
import time 

from scrape import scrape 
from app import get_db_connection

conn, cur = get_db_connection()
cur.execute("SELECT * FROM products")
links = cur.fetchmany(2)
conn.close()
linklist =[]
for link in links:
    linklist.append(link[0])

def start_scheduler(link):
    scheduler = BackgroundScheduler(timezone = "Asia/Kathmandu")
    scheduler.start()

    job = scheduler.add_job(scrape, 'interval', [link], seconds = 5)
    # print(job)

while True:
    for link in linklist:
        start_scheduler(link)
    time.sleep(20)


# for link in linklist:
#     scheduler = BackgroundScheduler(timezone = "Asia/Kathmandu")
#     scheduler.start()

#     # job = scheduler.add_job(scrape, 'cron', [now], hour = "21", minute = "48")
#     # Running scrape() at interval of every hour
#     job = scheduler.add_job(scrape, 'interval', [link], seconds = 5)
#     print(job)

#     while True:
#         time.sleep(3)