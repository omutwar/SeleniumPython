import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
gecko = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
# chrome = webdriver.Chrome(executable_path='drivers/chromedriver/chromedriver.exe')

drivers = ["gecko", "chrome"]
# drivers = [gecko]
# for driver in drivers:
#     if "chrome" in driver:
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         break
#     elif "firefox" in driver:
#         driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
#         break
#     else:
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         break


@pytest.mark.GoogleTitle
def test_google_page():
    for driver in drivers:
        option = Options()
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        driver.maximize_window()
        time.sleep(2)
        driver.get('https://www.google.com')
        time.sleep(2)
        print('Title of the page is: ' + driver.title)
        assert driver.title is not None and driver.title != ""
        print('Printing current website address: ' + driver.current_url)
        assert driver.current_url is not None
        print('Printing current website handle: ' + driver.current_window_handle)
        assert driver.current_window_handle is not None
        driver.close()


@pytest.mark.GoogleSearch
def test_google_signin():
    gecko.get("https://google.com")
    gecko.maximize_window()
    time.sleep(3)
    gecko.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('how to program with python')
    time.sleep(5)

    time.sleep(2)
    assert gecko.title is not None
    gecko.quit()
