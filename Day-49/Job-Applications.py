import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os

EMAIL_ID = os.environ["email"]
PASSWORD = os.environ["password"]
PHONE_NUMBER = os.environ["phone"]
URL = "https://www.linkedin.com/jobs/search/?currentJobId=2918373164&geoId=102713980&keywords=php%20developer&location=India"

# create a driver object for chrome
chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)


# loading the linked-in page using driver
driver.get(URL)
driver.maximize_window()

# clicks on sign in button
sign_in_page = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_page.click()

# sleeping for 3 sec so that till than the signin page will load without showing any errors
time.sleep(3)

# inserting email and password
mail = driver.find_element(By.ID, "username")
mail.send_keys(EMAIL_ID)
password = driver.find_element(By.ID, 'password')
password.send_keys(PASSWORD)
# click Enter to log in
password.send_keys(Keys.ENTER)


time.sleep(3)
# create list of all the jobs available in current page
jobs_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")


# store current window (browser tab) id, that will help us in final step, wait for that.
main_window_id = driver.current_window_handle


for job in jobs_list:
    # click on single job from jobs list using loop
    job.click()
    time.sleep(2)


#   created exception handling, because in some cases if any element isn't available, still our code will run perfectly
    try:
        # click on easy apply button
        easy_apply_click = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card button')
        easy_apply_click.click()
        time.sleep(5)
        # locate submit button element
        submit_button = driver.find_element(By.CSS_SELECTOR, ".justify-flex-end button .artdeco-button__text")
        # if submit button is available in page only then fill the form, otherwise it has multi steps to fill form.
        if submit_button.text == 'Submit application':
            add_number = driver.find_element(By.CSS_SELECTOR, '.fb-single-line-text input')
            # check if the text field is empty, only then enter your number
            if add_number.get_attribute("value") == "":
                add_number.send_keys(PHONE_NUMBER)
            submit_button.click()
            print('Applied')
            time.sleep(5)
            # I used another exception block because b/w the two upcoming situations only one occurs at a time.
            try:
                # after submitting form click cross to close the confirmation banner (either this will occur)
                click_cross = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__dismiss svg')
                click_cross.click()
            except NoSuchElementException:
                # after submission, sometimes there comes another pop up,so we need to close that as well on
                #                                                               left-hand side (or this will occur)
                click_dismiss = driver.find_element(By.CSS_SELECTOR, '.artdeco-toast-item__dismiss svg')
                click_dismiss.click()
        else:
            # in-case the submit button isn't available go back to the main menu using below steps
            back_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__dismiss')
            back_button.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__actionbar--confirm-'
                                                                  'dialog span')
            discard_button.click()

    # this is the main step of this project, that will make our project work properly even after errors.
    except NoSuchElementException:
        pass

    finally:
        time.sleep(2)
        # this will create list of all opened browser tab id's
        all_windows = driver.window_handles
        # this will close all tabs except the one which we want, that is jobs main page tab will remain open
        for tab in all_windows:
            if tab != main_window_id:
                driver.switch_to.window(tab)
                driver.close()
        # if we clicked on apply that will take us to another window, so this step will help us to redirect
        #                                                                                         to original main page
        driver.switch_to.window(main_window_id)
        time.sleep(3)


# driver.quit()
