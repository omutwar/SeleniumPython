"""
    Opera driver Page: <https://github.com/operasoftware/operachromiumdriver>

"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.binary_location = "path/to/operabrowser"
options.add_experimental_option('w3c', True)
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)

driver.get('https://www.google.com/')
input_txt = driver.find_element(By.NAME, 'q')
input_txt.send_keys('how to initialize selenium in python without binary file, write a demo test example')

time.sleep(5)  # see the result
driver.quit()
