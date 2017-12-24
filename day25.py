from selenium import webdriver
import requests
from bs4 import BeautifulSoup
'''
url = "http://www.chrisburkard.com/Shop"
web_r = requests.get(url)
web_soup = BeautifulSoup(web_r.text,"html.parser")
with open("normal.txt","w+") as normal_txt:
    for row in web_soup:
        normal_txt.write(str(row))

'''
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://www.chrisburkard.com/Shop")
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html,"html.parser")

with open("driver.txt","w+") as driver_txt:
    for row in sel_soup:
        driver_txt.write(str(row))