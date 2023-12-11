import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to a website
driver.get('http://www.google.com')
time.sleep(5)

# Remember to close the browser once done
driver.quit()
