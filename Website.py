import requests
from bs4 import BeautifulSoup


URL = 'https://www.amazon.in/Apple-iPhone-6S-Space-Storage/dp/B01LX3A7CC/ref=sr_1_1?keywords=apple&qid=1572036660&smid=A14CZOWI0VEHLG&sr=8-1'


headers = {
    "User-Agents": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
           }

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

title = soup.find(id= "productTitle").get_text()

print( title)
