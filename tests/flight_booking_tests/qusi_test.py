import time
"""
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

gecko_options = Options()
gecko_options.add_argument("detach", True)

driver_path = "drivers/geckodriver/geckodriver.exe"
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=gecko_options)
url = "https://www.travelocity.com/Flights"

n = 0
while n < 1_000_000:
    driver.get(url)
    print(n)
    time.sleep(3)
    n += 1
