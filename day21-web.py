import requests
from bs4 import BeautifulSoup

url = "https://www.jpmarumaru.com/tw/index.asp"
my_url = requests.get(url)

#print(my_url.text)

my_url_soup = BeautifulSoup(my_url.text,'html.parser')
print(my_url_soup)