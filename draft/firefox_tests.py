from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


def first_test():
    driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.yahoo.com")
    title = driver.title
    print(f'--- Current Title: {title}')
    assert 'Yahoo' in title
    driver.close()


if __name__ == '__main__':
    first_test()
