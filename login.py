from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)

def setURL():
    driver.get("https://gamesfi.live/")
    driver.maximize_window()
    print(driver.title)

def login():
#click on signup button
    signup_button= driver.find_element(By.XPATH, "//button[contains(text(),'LOGIN')]").click()

    Email= 'Farhan@yopmail.com'
    Password= 'Farhan@1234'

#Enter on email field
    email_field= driver.find_element(By.NAME,'email').send_keys(Email)

    #Enter password field
    password_field= driver.find_element(By.NAME,'password').send_keys(Password)

#click on login button
    login_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()

    time.sleep(2)

    actualerrormessage= driver.find_elements(By.CSS_SELECTOR, ".buxGtE")
    for error in actualerrormessage:
        print(error.text)

    time.sleep(2)

    driver.quit()

setURL()
login()