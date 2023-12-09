import requests
from bs4 import BeautifulSoup


URL = "https://news.google.com/home?hl=en-CA&gl=CA&ceid=CA:en"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")
AllH4 = soup.findAll("h4")

for healine in AllH4:
    print(healine.text, end="\n")