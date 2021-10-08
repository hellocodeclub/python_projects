from selenium import webdriver
import time
import random

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome('./chromedriver')
browser.get("https://login.aliexpress.com/")

user_input = browser.find_element_by_id('fm-login-id')
username = "email_here"
for letter in username:
    user_input.send_keys(letter)
    wait_time = random.randint(0,1000)/1000
    time.sleep(wait_time)

password_input = browser.find_element_by_id('fm-login-password')
time.sleep(1)
password = "your_password_here"
for letter in password:
    password_input.send_keys(letter)
    wait_time = random.randint(0,1000)/1000
    time.sleep(wait_time)

time.sleep(1)
try:
    slidebar_width = browser.find_element_by_css_selector("#nc_1__scale_text .nc-lang-cnt").size['width']
    time.sleep(2)
    slider_button = browser.find_element_by_css_selector('#nc_1_wrapper #nc_1_n1z')

    sliding_move = ActionChains(browser)
    sliding_move.click_and_hold(slider_button).move_by_offset(slidebar_width,0).release().perform()
    time.sleep(2)

except NoSuchElementException:
    pass

signin_button = browser.find_element_by_css_selector(".fm-login .fm-button")
signin_button.click()

browser.implicitly_wait(20)






