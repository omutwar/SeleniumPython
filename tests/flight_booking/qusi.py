from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


driver_path = "drivers/geckodriver/geckodriver.exe"
driver = webdriver.Firefox(executable_path=driver_path)
url = "https://www.travelocity.com/Flights"

n = 0
while n < 1_000_000:
    driver.get(url)
    print(n)
    time.sleep(3)
    n+=1
