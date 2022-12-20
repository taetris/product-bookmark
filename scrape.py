from bs4 import BeautifulSoup
import requests
import os
import sys
from datetime import datetime
import time
from db_connect import get_db_connection
# from app import get_db_connection, get_product

now = 'https://www.sastodeal.com/combo-set-of-3-pcs-tshirt-shorts-and-trackpants-sd-305396-1354-cms31.html'
here = "https://www.sastodeal.com/lnspirion-15-gaming-series-g5-i7-11800h-16gb-8x2-512gb-15-6-120hz-250nits-r-sd-dlpts-033.html"

itemList = []
# global itemName, price

def scrape(link):
    # conn, cur = get_db_connection()
    # cur.execute("SELECT * FROM products")
    # result = cur.fetchall()
    # conn.close() 
    url = requests.get(link)
    mainPage = BeautifulSoup(url.content, "html.parser")
    itemName = mainPage.find(["h1"], class_="page-title").get_text()
    price = (mainPage.find(["span"], class_="price").get_text()[3:]).replace(",", "")
    recentScrape = datetime.now()
    print("printing...", itemName, price)

    

    # output(itemName, price)
    return itemName, price


def output(itemName, price):
    output_itemName = itemName
    output_price = price
