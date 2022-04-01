from selenium import webdriver
import time
import random

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def login_with_username_and_password(browser, username, password):
    # FILL UP THE LOGIN FORM
    email_input = browser.find_element_by_css_selector('input[type=email]')

    email = username
    for letter in email:
        email_input.send_keys(letter)
        wait_time = random.randint(0,1000)/1000
        time.sleep(wait_time)

    next_button = browser.find_elements_by_css_selector("button")
    time.sleep(2)
    next_button[2].click()
    time.sleep(2)

    password_input = browser.find_element_by_css_selector('input[type=password]')
    password = password
    for letter in password:
        password_input.send_keys(letter)
        wait_time = random.randint(0,1000)/1000
        time.sleep(wait_time)

    next_button = browser.find_elements_by_css_selector("button")
    time.sleep(2)
    next_button[1].click()

    confirm_button = browser.find_elements_by_css_selector("div[role=button]")
    time.sleep(2)
    if(len(confirm_button)>0):
        confirm_button[1].click()

def click_on_agree_and_signin(browser):
    # agree_button= browser.find_element_by_css_selector('button')
    # time.sleep(2)
    # agree_button.click()

    signin_buttons= browser.find_elements_by_css_selector(".signin")
    time.sleep(6) # Wait longer so the message pops up
    while(len(signin_buttons)== 0):
        signin_buttons= browser.find_elements_by_css_selector(".signin")
        time.sleep(1)

    signin_buttons[0].click()

def enter_search_term(browser,search_term):
    # Enter text on the search term
    search_input = browser.find_element_by_id("search")
    for letter in search_term:
        search_input.send_keys(letter)
        wait_time = random.randint(0,1000)/1000
        time.sleep(wait_time)

    search_input.send_keys(Keys.ENTER)

def enter_comment(browser, comment):
    comment_input = browser.find_element_by_css_selector("ytd-comment-simplebox-renderer")

    entering_comment_actions = ActionChains(browser)

    entering_comment_actions.move_to_element(comment_input)
    entering_comment_actions.click()

    for letter in comment:
        entering_comment_actions.send_keys(letter)
        wait_time = random.randint(0,1000)/1000
        entering_comment_actions.pause(wait_time)

    entering_comment_actions.perform()

    time.sleep(1)

    send_comment_button = browser.find_element_by_id("submit-button")
    send_comment_button.click()

###########################################
#             BOT STARTS HERE             #
###########################################


from selenium import webdriver
firefoxProfile = webdriver.FirefoxProfile('/Users/martarey/Library/Caches/Mozilla/updates/Applications/Firefox/')
browser = webdriver.Firefox(firefoxProfile)
browser.get("https://www.youtube.com")

all_search_terms =['online marketing']#'motivation'

# Click Agree and Sing In
#click_on_agree_and_signin(browser)

# Sign In
#login_with_username_and_password(browser, "email", "password")

for search_term in all_search_terms:
    enter_search_term(browser, search_term)
    time.sleep(2)

    thumbnails = browser.find_elements_by_css_selector("ytd-video-renderer")

    for index in range(1,6):
        thumbnails[index].click()
        time.sleep(6)

        enter_comment(browser,"love it :)")
        browser.execute_script("window.history.go(-1)")
        thumbnails = browser.find_elements_by_css_selector("ytd-video-renderer")


time.sleep(1)
browser.close()






