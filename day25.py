import os
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
'''
#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://www.chrisburkard.com/Shop")
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html,"html.parser")

with open("driver.txt","w+") as driver_txt:
    for row in sel_soup:
        driver_txt.write(str(row))

'''

images = []
for i in sel_soup.findAll("img"):
    src = i["src"]
    images.append(src)

current_path = os.getcwd()
for img in images:
    try:
        file_name = os.path.basename(img)
        img_r = requests.get(img, stream=True)#打開 images 的網址連結
        new_path = os.path.join(current_path,"images",file_name)#目標是將圖片存到 images 這個資料夾內。
        with open(new_path,"wb") as output_file:
            shutil.copyfileobj(img_r,raw,output_file)#將網路上的 images 內容複製到目標檔案。
        del img_r#刪除已開啟的圖片連結
    except:
        pass



