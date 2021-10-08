#import webbrowser
#webbrowser.open('http://google.com', new=2)
#print("Open the browser")

# Selenium

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.google.com")


