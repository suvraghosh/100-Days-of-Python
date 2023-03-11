import requests
from bs4 import BeautifulSoup
import smtplib
# import lxml

URL = "https://www.amazon.com/Beats-Studio-Cancelling-Earbuds-Built-Bluetooth-Headphones/dp/B096SRYXMP/ref=sr_1_4?crid=3MN86PO1UDRM4&keywords=airpods&qid=1678541587&sprefix=airpod%2Caps%2C576&sr=8-4"
YOUR_EMAIL = MY_EMAIL
YOUR_PASSWORD = MY_PASSWORD

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
           "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,bn;q=0.6"}
response = requests.get(URL, headers=headers)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")

product_price = soup.find(name="span", class_="a-offscreen")
price_detail = product_price.getText()
price_without_currency = float(price_detail.split("$")[1])

product_title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 120

if price_without_currency < BUY_PRICE:
    message = f"{product_title} is now {price_detail}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )

