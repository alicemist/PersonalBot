from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = "C:/chrome/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = brave_path

# Belirli bir kullanıcı profilini yüklemek için:
profile_path = "C:/Users/ozkar/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default"
chrome_options.add_argument(f'user-data-dir={profile_path}')

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.example.com")
