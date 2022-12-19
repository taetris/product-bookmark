from bs4 import BeautifulSoup
import requests
import os
import sys
from datetime import datetime
import time
# from app import get_db_connection, get_product

now = 'https://www.sastodeal.com/combo-set-of-3-pcs-tshirt-shorts-and-trackpants-sd-305396-1354-cms31.html'
here = "https://www.sastodeal.com/lnspirion-15-gaming-series-g5-i7-11800h-16gb-8x2-512gb-15-6-120hz-250nits-r-sd-dlpts-033.html"

itemList = []


def scrape(link):
    url = requests.get(link)
    # print("Current Link: ", link)
    html = BeautifulSoup(url.content, "html.parser")
    mainPage = html
    itemName = mainPage.find(["h1"], class_="page-title").get_text()
    FirstScrape = datetime.now()
    # print(FirstScrape)
    time.sleep(3)
    FirstPrice = (mainPage.find(["span"], class_="price").get_text()[3:]).replace(",", "")
    recentScrape = datetime.now()
    # new_price = main_page.find(["span"], class_="price").get_text()[3:]
    # reduced = (float(new_price) - float(first_price))*100
    # lowest_price = new_price if new_price > first_price else first_price
    lowestPrice = datetime.now()
    # print("Title: ", item_name, "Date scraped:", first_scrape, "Price:",first_price)
    info_list = [itemName, FirstPrice]
    print(info_list)
    
    # return info_list

# while True:
#     time.sleep(10)
#     print(scrape(now))
