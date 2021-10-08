from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome('./chromedriver')
browser.get("https://login.aliexpress.com/")

user_input = browser.find_element_by_id('fm-login-id')
user_input.send_keys("email_here")

password_input = browser.find_element_by_id('fm-login-password')
time.sleep(1)
password_input.send_keys("your_password_here")
time.sleep(1)
password_input.send_keys("-")

slidebar_width = browser.find_element_by_css_selector("#nc_1__scale_text .nc-lang-cnt").size['width']

time.sleep(2)
slider_button = browser.find_element_by_css_selector('#nc_1_wrapper #nc_1_n1z')

sliding_move = ActionChains(browser)
sliding_move.click_and_hold(slider_button).move_by_offset(slidebar_width,0).release().perform()
time.sleep(2)

signin_button = browser.find_element_by_css_selector(".fm-checkcode .fm-button")
signin_button.click()

browser.implicitly_wait(20)






