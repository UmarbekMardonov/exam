from bs4 import BeautifulSoup
import requests

"""
URL = "https://www.stadion.uz/"
r = requests.get(URL)

soup = BeautifulSoup(r.text, "html.parser")
'''
table = soup.find(id="scorers_place")
tr = table.find_all('tr')
for tr_single in tr:
    for td in tr_single.find_all('td'):
        print(td.text, end=" | ")
    print()

'''

table = soup.find(id="online_tablo")
tit = table.find_all(id="online_tablo_title")
for i in tit:
    for p in i:
        print(p.text, end=" | ")
    print()
"""

URL = "https://www.olx.uz/nedvizhimost/"
r = requests.get(URL)

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find(class_="css-oukcj3")
obj = table.find_all(class_='css-1sw7q4x')
for obj_single in obj:
    for ads in obj_single:
        for ads_single in ads:
            print(ads_single.text, end=" | ")
            img = ads_single.find("img")
            print(img)
        print()
