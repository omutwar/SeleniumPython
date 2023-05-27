from selenium import webdriver
import time

gecko = webdriver.Firefox(executable_path='bin/geckodriver/geckodriver.exe')
chrome = webdriver.Chrome(executable_path='bin/chromedriver/chromedriver.exe')

drivers = [gecko, chrome]


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
