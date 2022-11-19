from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)

def setURL():
    driver.get("https://gamesfi.live/")
    driver.maximize_window()
    print(driver.title)

def contactus():

    contact_us=driver.find_element(By.XPATH,"//a[contains(text(),'Contact us')]").click()
    time.sleep(2)
    enter_name= driver.find_element(By.NAME, 'name').send_keys("Test Acccount")
    enter_email=driver.find_element(By.NAME,'email').send_keys('test@yopmail.com')
    message= driver.find_element(By.NAME,'message').send_keys("Testing Contact us")
    submit_btn= driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
    time.sleep(3)
    driver.quit()

setURL()
contactus()