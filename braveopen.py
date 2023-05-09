import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

driver_path = "C:/chrome/chromedriver.exe"

url = "https://chat.openai.com/?model=gpt-4"
xpath1 = "//*[text() = 'Log in']"
xpath2 = "//*[text() = 'Continue with Google']"
xpath3 = "//*[text() = 'alicemozkara@gmail.com']"

chrome_options = webdriver.ChromeOptions()

# Chrome profilini "Kişi 1" olarak ayarla
chrome_options.add_argument("--profile-directory=Default")

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

    element3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath3))
    )
    element3.click()

except Exception as e:
    print(f"Hata: {e}")
