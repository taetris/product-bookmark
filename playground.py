import requests
from bs4 import BeautifulSoup

link = "https://www.sastodeal.com/baltra-dream-electric-rice-cooker-2-8-litre-bdt1000-btd-1000d.html"
# link = "https://www.sastodeal.com/indpro-legend-football-shoes-orange-sd-275646-1381-rkolay-c1106-001.html"
url = requests.get(link)
mainPage = BeautifulSoup(url.content, "html.parser")
itemName = mainPage.find(["h1"], class_="page-title").get_text()
# price = (mainPage.find(["span"], class_="pricenew").get_text()[4:]).replace(",", "") 
# price= mainPage.find('span', {'data-price-type': 'finalPrice'}).text()
# print(itemName, price)
# soup = BeautifulSoup(html, 'html.parser')
price = (mainPage.find('span', {'data-price-type': 'finalPrice'})).find('span', {'class': 'price'}).get_text()[3:].replace(",", "") 
# price = price_element.text()
print(price)  


