from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class BaseClass:
    """
        This is the base class, here we can define most of the common methods that's used during the test.

        Example:
            - initiate the driver
            -
    """

    # This will maximize the window at startup
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


    def __init__(self, driver):
        self.driver = driver
        self.username_text_box = ()
        self.password_text_box = ()


    def get_driver(self, driver):
        pass

    def open_browser(self, url):
        self.driver.get(url)

    def do_login(self, username, password):
        self.driver.find_element(By.ID, '').send_keys("")
        self.driver.find_element(By.NAME, '').send_keys("")
