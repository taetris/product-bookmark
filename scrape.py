from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time
from db_connect import get_db_connection

def scrape(link):

    url = requests.get(link)
    mainPage = BeautifulSoup(url.content, "html.parser")
    itemName = mainPage.find(["h1"], class_="page-title").get_text()
    # price = (mainPage.find_all(["span"], class_="price")[-1].get_text()[3:]).replace(",", "") or (mainPage.find(class_='normal-price pricenew').get_text()[3:]).replace(",", "")
    price = (mainPage.find('span', {'data-price-type': 'finalPrice'})).find('span', {'class': 'price'}).get_text()[3:].replace(",", "") 
    recentScrape = datetime.now()
    print("printing...", itemName, price)

    return itemName, price


