from apscheduler.schedulers.background import BackgroundScheduler

def scrape():
    print("hiiiii")

scheduler = BackgroundScheduler(timezone = "Asia/Kathmandu")
scheduler.start()
link = "https://www.sastodeal.com/lnspirion-15-gaming-series-g5-i7-11800h-16gb-8x2-512gb-15-6-120hz-250nits-r-sd-dlpts-033.html"

job = scheduler.add_job(scrape, 'interval', seconds = 5)
    
