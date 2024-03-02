"""
    This class provides browser types for different browser
"""
from selenium import webdriver
from utils.config_reader import ConfigReader


class DriverFactory:
    @staticmethod
    def get_webdriver():
        browser_type = ConfigReader.get_property('browsers', 'browser')
        if browser_type.lower() == 'firefox':
            return webdriver.Firefox()
        elif browser_type.lower() == "chrome":
            return webdriver.Chrome()
        elif browser_type.lower() == "edge":
            return webdriver.Edge()
        else:
            raise ValueError("Unsupported Browser Type")


driver = DriverFactory.get_webdriver()
driver.maximize_window()
driver.get("https://www.google.com")
title = driver.title
print(f'*** Current Title: {title}')
