import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
url = "https://www.travelocity.com/Flights"

n = 0
while n < 3:
    driver.get(url)
    print(n, " : ", driver.title)
    time.sleep(1)
    n += 1
    driver.delete_all_cookies()
    # not closing the driver here to keep the session open

driver.close()
