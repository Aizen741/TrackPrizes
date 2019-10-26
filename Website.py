import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Apple-iPhone-6S-Space-Storage/dp/B01LX3A7CC/ref=sr_1_1?keywords=apple&qid=1572036660&smid=A14CZOWI0VEHLG&sr=8-1'

headers = {
    "User-Agents": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_dealprice").get_text()
    converted_price = int(price[0:6])

    if (converted_price < 23000):
        send_mail()

    print(converted_price)
    print(title.strip())

    if (converted_price > 23000):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('das81573@gmail.com', '********')
    subject = "The Price is low now"
    body = "Check the link : 'https://www.amazon.in/Apple-iPhone-6S-Space-Storage/dp/B01LX3A7CC/ref=sr_1_1?keywords=apple&qid=1572036660&smid=A14CZOWI0VEHLG&sr=8-1'"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'das81573@gmail.com',
        'rahulsivadas2009@gmail.com',
        msg
    )
    print("Hey Email has been send")

    server.quit()


check_price()
