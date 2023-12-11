import selenium.webdriver.chrome.webdriver

from POMDemo.base_classes.BaseClass import BaseClass


class LandingPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)


def test_add_numbers(a, b):
    return a + b


lp1 = LandingPage()
