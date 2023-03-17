import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLScTFiuzlBPwxeWoisuOkoV1hCJz_L7BSQBUhizdIiIK7ONGtQ/viewform"

URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B" \
      "%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.69234177970014%2C" \
      "%22north%22%3A37.85814816331502%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B" \
      "%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22" \
      "%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B" \
      "%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C" \
      "%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22" \
      "%3Atrue%7D"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/110.0.0.0 Safari/537.36",
           "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,bn;q=0.6"}
response = requests.get(URL, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_rental_links = soup.find_all(name="a", class_="property-card-link")
rental_links = []
for links in all_rental_links:
    rental = links.get("href")
    if "href" not in rental:
        rental_links.append(f"https://www.zillow.com{rental}")
    else:
        rental_links.append(rental)
# print(rental_links)

all_rental_addresses = soup.find_all(name="address")
rental_addresses = [address.get_text().split(" | ")[-1] for address in all_rental_addresses]
# print(rental_addresses)

# all_price_elements = soup.select(".list-card-details li")
# all_prices = [price.get_text().split("+")[0] for price in all_price_elements if "$" in price.text]
# print(all_prices)

for n in range(len(rental_links)):

    driver.get(GOOGLE_FORM)
    sleep(5)
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                            '1]/div/div[1]/input')
    sleep(5)
    address.send_keys(rental_addresses[n])
    link = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div["
                                         "2]/div/div["
                                         "1]/div/div[1]/input")
    sleep(5)
    link.send_keys(rental_links[n])
    submit_button = driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")
    submit_button.click()


# price.send_keys(all_prices[n])
