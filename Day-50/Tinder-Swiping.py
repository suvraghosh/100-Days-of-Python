import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

FB_EMAIL = YOUR_FACEBOOK_EMAIL
FB_PASSWORD = YOUR_FACEBOOK_PASSWORD

# create a driver object for chrome
chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

URL = "https://tinder.com/"
driver.get(URL)
click_log_in = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
click_log_in.click()
time.sleep(10)
facebook = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div")
facebook.click()
# time.sleep(10)

# pop-up facebook log in page in anew window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Login using facebook
email = driver.find_element(By.ID, "email")
email.send_keys(FB_EMAIL)
password = driver.find_element(By.ID, "pass")
password.send_keys(FB_PASSWORD)
time.sleep(10)
log_in_btn = driver.find_element(By.ID, "loginbutton")
log_in_btn.click()
time.sleep(10)

driver.switch_to.window(base_window)
print(driver.title)
time.sleep(10)

# Dismiss all requests
allow_location = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]")
allow_location.click()
time.sleep(20)
notification_pop_up = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]")
notification_pop_up.click()
time.sleep(20)
cookies_pop_up = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]")
cookies_pop_up.click()
time.sleep(20)

# Hit likes
for n in range(20):
    time.sleep(2)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span/svg")
        like_button.click()
    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            print("ElementClickInterceptedException")
            time.sleep(5)
            match_pop = driver.find_element(By.XPATH, "//*[@id='q-71405977']/main/div/div[1]/div/div[4]/button")
            match_pop.click()
        except NoSuchElementException:
            print("NoSuchElementException")
            time.sleep(5)

driver.quit()
