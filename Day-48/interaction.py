from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Use Selenium to Scrape Website Data

chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

# 1. Scrapping Wikipedia Website Data

"""
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)
"""
# Interacting with website by automated bot

"""
article_count.click()
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
"""

# 2. Scrapping and Interacting With W3 Schools Website To Sign Up

driver.get("https://profile.w3schools.com/sign-up?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com%2F")
email = driver.find_element(By.NAME, "email")
email.send_keys("YourEmail@gmail.com")
password = driver.find_element(By.NAME, "new-password")
password.send_keys("YourPassword")
sign_up_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div[1]/div/div[5]/div[1]/button")
sign_up_btn.click()
