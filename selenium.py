from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

"""
URL = "https://www.stadion.uz/"
r = requests.get(URL)

soup = BeautifulSoup(r.text, "html.parser")

table = soup.find(id="scorers_place")
tr = table.find_all('tr')
for tr_single in tr:
    for td in tr_single.find_all('td'):
        print(td.text, end=" | ")
    print()


table = soup.find(id="online_tablo")
tit = table.find_all(id="online_tablo_title")
for i in tit:
    for p in i:
        print(p.text, end=" | ")
    print()

# olx

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



def pageBottom(driver):
    bottom = False
    a = 0
    while not bottom:
        new_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(f"window.scrollTo(0, {a});")
        if a > new_height:
            bottom = True
        a += 5


driver = webdriver.Chrome()
driver.maximize_window()
for i in range(1, 5):
    driver.get(f"https://www.olx.uz/list/q-dacha/?page={i}")
    time.sleep(2)
    pageBottom(driver)  # <---Go to Bottom
    time.sleep(2)
    assert "No results found." not in driver.page_source
    res = driver.page_source

    soup = BeautifulSoup(res, "html.parser")
    tablo = soup.find("div", attrs={"data-testid": "listing-grid"})
    items = tablo.find_all("div", attrs={"data-cy": "l-card"})
    print(items)
    for item in items:
        print(item.find("img"))

driver.close()
"""


def pageBottom(driver):
    bottom = False
    a = 0
    while not bottom:
        new_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(f"window.scrollTo(0, {a});")
        if a > new_height:
            bottom = True
        a += 5


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.olx.uz/")
# table = driver.find_element(By.CLASS_NAME, "css-zs6l2q")
# table.click()
# time.sleep(3)
# email_input = driver.find_element(By.NAME, "username")
# parol_input = driver.find_element(By.NAME, "password")
# email_input.click()
# time.sleep(2)
# email_input.send_keys("umarbekpython@gmail.com")
# parol_input.click()
# time.sleep(2)
#
# parol_input.send_keys("Um92211002" + Keys.ENTER)
# time.sleep(5)
search_input = driver.find_element(By.ID, 'search')
search_input.click()
time.sleep(2)
search_input.send_keys("hyundai tucson" + Keys.ENTER)
time.sleep(2)
like_button_xpath = "//span[@data-testid='adAddToFavorites']//div[@data-testid='favorite-icon']"
like_button = driver.find_element(By.XPATH, like_button_xpath)
print(like_button)
# like_button.click()
time.sleep(3)
pageBottom(driver)
time.sleep(5)
assert "No results found." not in driver.page_source
res = driver.page_source
# soup = BeautifulSoup(res, "html.parser")
# table = soup.find(class_='css-zs6l2q')
# table.click()
# email_input = soup.find(name="username")
# print(email_input)
