from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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

def login():
#click on signup button
    signup_button= driver.find_element(By.XPATH, "//button[contains(text(),'LOGIN')]").click()

    Email= 'Farhan@yopmail.com'
    Password= 'Farhan@12345'

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

def changepassword():
    element = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CLASS_NAME, 'dropdown')))

    menu_btn = driver.find_element(By.CLASS_NAME, 'dropdown').click()

    change_password = driver.find_elements(By.CLASS_NAME, 'dropdown-item')
    time.sleep(1)
    change_password[0].click()

    if driver.find_element(By.NAME, 'oldPassword').is_displayed():
        old_password = driver.find_element(By.NAME, 'oldPassword').send_keys('Farhan@12345')
        new_password = driver.find_element(By.NAME, 'newPassword').send_keys('Farhan@12345')
        confirm_password = driver.find_element(By.NAME, 'confirmPassword').send_keys('Farhan@12345')
        save_btn = driver.find_element(By.CLASS_NAME, 'hywa-Dz').click()
        time.sleep(2)
        actualerrormessage = driver.find_elements(By.CSS_SELECTOR, ".buxGtE")
        for error in actualerrormessage:
            print(error.text)
    else:
        print("Element is not present")

    time.sleep(2)
    driver.quit()

setURL()
login()
changepassword()