from apscheduler.schedulers.background import BackgroundScheduler
import time 

from scrape import scrape 

now = 'https://www.sastodeal.com/combo-set-of-3-pcs-tshirt-shorts-and-trackpants-sd-305396-1354-cms31.html'
scheduler = BackgroundScheduler(timezone = "Asia/Kathmandu")
scheduler.start()

# job = scheduler.add_job(scrape, 'cron', [now], hour = "21", minute = "48")
# Running scrape() at interval of every hour
job = scheduler.add_job(scrape, 'interval', [now], hour = 1)
print(job)

while True:
    time.sleep(1)