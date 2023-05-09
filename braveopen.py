import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

load_dotenv()

driver_path = "C:/chrome/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

url = "https://chat.openai.com/?model=gpt-4"
xpath1 = "//*[text() = 'Log in']"
xpath2 = "//*[text() = 'Continue with Google']"

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--profile-directory=Default")
chrome_options.binary_location = brave_path

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

try:
    element1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath1))
    )
    element1.click()

    element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath2))
    )
    element2.click()

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    email_input.send_keys(email)

    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "identifierNext"))
    )
    next_button.click()

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys(password)

    password_next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "passwordNext"))
    )
    password_next_button.click()

except Exception as e:
    print(f"Hata: {e}")
