from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)

def setURL():
    driver.get("https://gamesfi.live/")
    driver.maximize_window()
    print(driver.title)

def signup():
#click on signup button
    signup_button= driver.find_element(By.XPATH, "//button[contains(text(),'SIGN UP')]").click()

    Email= 'Farhan@yopmail.com'
    Password= 'Farhan@1234'
    Referalcode= "9eallw"

#Enter on email field
    email_field= driver.find_element(By.NAME,'email').send_keys(Email)

    #Enter password field
    password_field= driver.find_element(By.NAME,'password').send_keys(Password)

#Enter referal code
    referal_code= driver.find_element(By.NAME, 'referred_by').send_keys(Referalcode)

#checkbox
    checkbox_click= driver.find_element(By.NAME, 'privacypolicy').click()

#click on signup button
    signup_buton= driver.find_element(By.CLASS_NAME, 'mt-3').click()

    time.sleep(2)

    actualerrormessage= driver.find_elements(By.CSS_SELECTOR, ".buxGtE")
    for error in actualerrormessage:
        print(error.text)
    time.sleep(3)

    driver.quit()

setURL()
signup()