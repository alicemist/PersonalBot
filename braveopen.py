import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

load_dotenv()
username = os.getenv("email")
password = os.getenv("PASSWORD")
print(username)
def login_leetcode(driver, username, password):
    xpath1 = "//*[text() = 'Sign in']"
    xpath2 = "//*[@id='id_login']"
    username_xpath = "//*[@id='id_login']"
    password_xpath = "//*[@id='id_password']"
    login_button_xpath = "//*[text() = 'Sign In']"
   

    try:
        element1 = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, xpath1))
        )
        element1.click()
        loading_element_xpath = "//div[@id='initial-loading']"
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, loading_element_xpath))
        )
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, username_xpath))
        )

        username_input.click()
        username_input.send_keys(username)
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, password_xpath))
        )

        password_input.click()
        password_input.send_keys(password)

        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, login_button_xpath))
        )
        login_button.click()

    except Exception as e:
        print(f"Hata: {e}")

driver_path = "C:/chrome/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path

profile_path = "C:/Users/ozkar/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default"
chrome_options.add_argument(f'user-data-dir={profile_path}')

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://leetcode.com/problemset/all/"
driver.get(url)


login_leetcode(driver, username, password)

try:
        questionpathxpath = "//*[@role= 'rowgroup'][1]/div[1]"
        question_element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, questionpathxpath))
        )
        question_element.click()
except Exception as e:
        print(f"Soru elementine tıklama sırasında hata: {e}")