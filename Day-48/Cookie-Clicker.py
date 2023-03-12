from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import time

# Use Selenium to Scrape Website Data

chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

# Get cookie to click on.
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

game_is_on = True
count = 1
time_out = time() + 5
i_want_30 = time() + (60 * 30)


def click():
    cookie.click()


def buy_items():
    item_prices = driver.find_elements(By.CSS_SELECTOR, "#store b ")
    for item in reversed(item_prices):

        if item.text != "":

            price = int(item.text.replace(",", "").split("-")[1].replace(" ", ""))
            item_id = item.text.split("-")[0].replace(" -  ", "").rstrip()
            final_id = f"buy{item_id}"

            if money >= price:
                store_item = driver.find_element(By.ID, final_id)
                store_item.click()
                print(f"buying {item_id}")
                return


while game_is_on:
    money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
    click()
    if time() > time_out:
        buy_items()
        time_out = time() + 5
        if time() > i_want_30:
            game_is_on = False
            cookie_per_min = driver.find_element(By.ID, "cps")
            print(cookie_per_min)

driver.close()
