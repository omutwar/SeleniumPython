import time

from selenium import webdriver

driver_path = "drivers/geckodriver/geckodriver.exe"
driver = webdriver.Firefox(executable_path=driver_path)
url = "https://www.travelocity.com/Flights"

n = 0
while n < 1_000_000:
    driver.get(url)
    print(n)
    time.sleep(3)
    n += 1
