from bs4 import BeautifulSoup
import requests
import json
import os
import sys
from datetime import datetime

link = "https://www.sastodeal.com/electronic/laptops.html"
json_file = "files/all_scrapes.json"

with open("files/laptop_scrape.json", "w") as f:
    f.close()

def scrape():
    url = requests.get(link)
    # print("Current Link: ", link)
    html = BeautifulSoup(url.content, "html.parser")
    item_list = []
    main_page = html
    item_name = main_page.find(["a"], class_="product-item-link").get_text()
    price = main_page.find(["span"], class_="price").get_text()

item_info = {
    "item_name": item_name,
    "price": price,
    "first_scrape": datetime.now(),
    "recent_scrape": None,
    "reduced": None
}

with open("files/laptop_scrape.json", "r+") as f:
    file_data = json.load(f)
    try:
       
        if item_name in json_dict["item_name"]:
            scrape()
            if (price<json_dict["price"]):
                print("price dropped")
                json_dict["recent_scrape"] = datetime.now()
                reduced = (json_dict["price"] - price)
                json_dict["price"] = price
        
    except AttributeError: # new item
        item_list.append(item_info)





