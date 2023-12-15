from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager

search_site = "https://www.yahoo.com"


# Configure Options and Service
gecko_options = Options()
gecko_options.add_experimental_option("detach", True)
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=gecko_options)


class YahooSearchTests:

    """
        This is Yahoo search Tests
    """
    def test_search_books(self, item: str):
        driver.get(search_site)


    def test_search_news(self, topic: str):
        driver.get(topic)
        title = driver.title()
        print(title)

