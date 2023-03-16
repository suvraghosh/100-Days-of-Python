from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementClickInterceptedException

from time import sleep

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
service = ChromeService("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=option)

INSTA_USERNAME = YOUR USERNAME
INSTA_PASSWORD = YOUR PASSWORD


class InstaFollower:
    def __init__(self):
        self.fb = None
        self.driver = driver

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(INSTA_USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(INSTA_PASSWORD)
        sleep(5)
        login = self.driver.find_element(By.XPATH,
                                         "/html/body/div[2]/div/div/div[1]/div/div/div/div["
                                         "1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
        login.click()
        sleep(5)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/geeks_for_geeks/")
        sleep(10)
        check_follower = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div["
                                                            "1]/div[2]/section/main/div/header/section/ul/li[2]/a/div")
        check_follower.click()
        sleep(5)
        pop_up_window = WebDriverWait(
            driver, 2).until(expected_conditions.element_to_be_clickable(
            (By.XPATH,
             "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")))

        # Scroll till Followers list is there
        while True:
            driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window)
            sleep(1)

    def follow(self):
        # Number of followers
        number_of_followers = self.driver.find_element(By.XPATH,
                                                       "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div["
                                                       "1]/div[2]/section/main/div/header/section/ul/li["
                                                       "2]/a/div/span/span")
        number = int(number_of_followers.text.split(' ')[0].strip()) * 1000

        # Follow all the followers
        for i in range(1, number):
            try:
                follow = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div["
                                                            "2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div["
                                                            "1]/div/div/div/div[3]/div/button/div")
                follow.click()
                sleep(2)
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follow)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div["
                                                                   "2]/div/div/div[1]/div/div[2]/div/div/div/div/div["
                                                                   "2]/div/div/div[3]/button[2]")
                cancel_button.click()
                sleep(1)


insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
