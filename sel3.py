from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument("--headless")
driver=webdriver.Firefox(firefox_options=options)
driver.get("https://www.facebook.com")
wait = WebDriverWait(driver, 600)
email=driver.find_element_by_id('email')
email.send_keys('Your email/phone_number goes here')
print("Email Entered")
pwd=driver.find_element_by_id('pass')
pwd.send_keys('Your password goes here')
print("Password entered")
button=driver.find_element_by_id("loginbutton")
button.click()
print("Login Successfull")
search=driver.find_element_by_name("xhpc_message")
#change this message to the status that you want to upload
search.send_keys("This post is uploaded by a python script :) Enjoy coding")
search.submit()