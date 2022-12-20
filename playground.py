from apscheduler.schedulers.background import BackgroundScheduler
from scrape import scrape
def scrape():
    print("hiiiii")

# scheduler = BackgroundScheduler(timezone = "Asia/Kathmandu")
# scheduler.start()
# link = "https://www.sastodeal.com/lnspirion-15-gaming-series-g5-i7-11800h-16gb-8x2-512gb-15-6-120hz-250nits-r-sd-dlpts-033.html"

# job = scheduler.add_job(scrape, 'interval', seconds = 5)
    
linklist = [
    'https://www.sastodeal.com/combo-set-of-3-pcs-tshirt-shorts-and-trackpants-sd-305396-1354-cms31.html',
    'https://www.sastodeal.com/samsung-galaxy-a70-6gb-ram-128gb-rom-white-sd-109656-229-sbox-ywrs-0916005.html',
    'https://www.sastodeal.com/youwe-stand-fan-without-remote-youwe-standfan.html',
    'https://www.sastodeal.com/lnspirion-15-gaming-series-g5-i7-11800h-16gb-8x2-512gb-15-6-120hz-250nits-r-sd-dlpts-033.html',
    'https://www.sastodeal.com/lnspirion-15-gaming-series-g5-i7-11800h-16gb-8x2-512gb-15-6-120hz-250nits-r-sd-dlpts-033.html',
    ''

]
for link in linklist:
    scheduler = BackgroundScheduler(timezone = "Asia/Kathmandu")
    scheduler.start()

    # job = scheduler.add_job(scrape, 'cron', [now], hour = "21", minute = "48")
    # Running scrape() at interval of every hour
    job = scheduler.add_job(scrape, 'interval', [link], seconds = 5)
    print(job)

    while True:
        time.sleep(3)
