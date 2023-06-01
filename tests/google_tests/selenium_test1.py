import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

gecko = webdriver.Firefox(executable_path='bin/geckodriver/geckodriver.exe')
chrome = webdriver.Chrome(executable_path='bin/chromedriver/chromedriver.exe')

drivers = [gecko, chrome]


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
    chrome.get("https://google.com")
    chrome.maximize_window()
    time.sleep(3)
    chrome.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('how to program with python')
    time.sleep(5)

    time.sleep(2)
    assert chrome.title is not None
    chrome.quit()
