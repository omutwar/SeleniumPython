from selenium import webdriver
import time

gecko = webdriver.Firefox(executable_path='bin/geckodriver/geckodriver.exe')
chrome = webdriver.Chrome(executable_path='bin/chromedriver/chromedriver.exe')

drivers = [gecko, chrome]

for driver in drivers:
    driver.maximize_window()
    time.sleep(2)
    driver.get('https://www.google.com')
    time.sleep(2)
    print('Title of the page is: ' + driver.title)
    print('Printing current website address: ' + driver.current_url)
    print('Printing current website handle: ' + driver.current_window_handle)
    driver.close()
