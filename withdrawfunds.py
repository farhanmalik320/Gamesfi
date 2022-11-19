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


def withdraw():

  element=WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CLASS_NAME,'losDLa')))

  #click on withdraw button
  withdraw_button= driver.find_element(By.CLASS_NAME,'losDLa').click()

  element = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CLASS_NAME,'button-active')))

  #active withdraw menu

  withdraw_button= driver.find_element(By.CLASS_NAME,'button-active').click()

  element = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]')))
  #click on gamedrop down
  game_dropdown= driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]').click()

  element = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[2]/div[2]/input[1]')))

  #click on checkbox
  checkbox_click= driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[2]/div[2]/input[1]').click()

  element = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/button[1]')))

#click on save button
  save_button= driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/button[1]').click()

  driver.execute_script("window.scrollBy(0,500)")

  element = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]')))

#click on payout
  payout_dropdown= driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]').click()

  element = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[2]/div[2]/input[1]')))

#select BTC
  currency_BTC= driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[2]/div[2]/input[1]').click()

  element = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/button[1]')))

#click on save
  save=driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/button[1]').click()

#click on Max
  Max_button= driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[2]/button[1]').click()

#Add email
  Email_address= driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/input[1]').send_keys('Farhan.sharif@ideofuzion.com')

#cash_button
  cashout_button= driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/button[1]').click()

#click on withdraw button
  withdraw_buttton= driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[3]/div[1]/button[2]').click()

  time.sleep(2)
  actualerrormessage = driver.find_elements(By.CSS_SELECTOR, ".buxGtE")
  for error in actualerrormessage:
      print(error.text)

  time.sleep(5)

#click on history tab
  history_tab= driver.find_element(By.CLASS_NAME, 'button-one').click()


setURL()
login()
withdraw()