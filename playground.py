import requests
from bs4 import BeautifulSoup

link = 'https://www.sastodeal.com/king-size-moto-vella-cotton-bed-sheet-set-slkw026.html'
url = requests.get(link)
mainPage = BeautifulSoup(url.content, "html.parser")
itemName = mainPage.find(["h1"], class_="page-title").get_text()
price = mainPage.find_all("span", class_="price")[-1]
# price = [e for e in price if e.find("span", class_="special-price")]


print(itemName, price)




#     # job = scheduler.add_job(scrape, 'cron', [now], hour = "21", minute = "48")
#     # Running scrape() at interval of every hour
#     # job = scheduler.add_job(scrape, 'interval', [link], seconds = 5)
#     # print(job)
    



