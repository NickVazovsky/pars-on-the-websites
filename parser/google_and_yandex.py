"""from bs4 import BeautifulSoup
import requests

url ='http://www.google.com/search?q='
page = requests.get(url + 'кузнецовский фарфор')
check = 'http://kuznetsovskyfarfor.ru/'
soup = BeautifulSoup(page.text)
h3 = soup.find_all("h3",class_="r")
index = 1
for elem in h3:
  elem=elem.contents[0]
  if check in elem['href']:
    print(index)
  else:
    index+=1
   """
from bs4 import BeautifulSoup
import requests

check = "http://redkie.ru"
url = 'http://www.google.com/search?q='
page = requests.get(url + 'кузнецовский фарфор')
index2=1
for index in range(10):
    soup = BeautifulSoup(page.text)
    next_page = soup.find("a", class_="fl")
    next_link = ("https://www.google.com" + next_page["href"])
    print(next_link)
    h3 = soup.find_all("h3", class_="r")
    for elem in h3:
        elem = elem.contents[0]
        if check in elem['href']:
            print(index2)
        else:
            index += 1
    page = requests.get(next_link)





    
