import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

gecko = webdriver.Firefox(executable_path='drivers/geckodriver/geckodriver.exe')
# chrome = webdriver.Chrome(executable_path='drivers/chromedriver/chromedriver.exe')

# drivers = [gecko, chrome]
drivers = [gecko]


@pytest.mark.GoogleTitle
def test_google_page():
    for driver in drivers:
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
