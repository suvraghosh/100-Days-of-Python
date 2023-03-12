from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Use Selenium to Scrape Website Data

chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

# 1. Scrapping Amazon Website Data

"""

driver.get("https://www.amazon.com/Beats-Studio-Cancelling-Earbuds-Built-Bluetooth-Headphones/dp/B096SRYXMP/ref=sr_1_4?crid=3MN86PO1UDRM4&keywords=airpods&qid=1678541587&sprefix=airpod%2Caps%2C576&sr=8-4")
price = driver.find_element(By.CLASS_NAME, 'a-offscreen')
price = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[1]')
print(price.text)

"""


# 2. Scrapping Python Website Data

driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_name[n].text,
    }
print(events)


# driver.close()
driver.quit()
