"""
    Opera driver Page: <https://github.com/operasoftware/operachromiumdriver>
"""

import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@allure.feature("Google Title Test")
@allure.story("Valid User Login")
def google_title_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', True)
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    driver.get('https://www.google.com/')
    title = driver.title
    print(f'*** Current Title: {title}')
    assert 'Google' in title

    input_txt = driver.find_element(By.NAME, 'q')
    input_txt.send_keys('how to initialize selenium in python without binary file, write a demo test example')
    input_txt.send_keys(Keys.ENTER)

    time.sleep(5)  # see the result
    driver.quit()


def test_playwright_site():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://playwright.dev")
    title = driver.title
    print(f'<test_playwright_site> test :: Current Title: {title}')
    assert 'Playwright' in title
    driver.close()


if __name__ == '__main__':
    google_title_test()
