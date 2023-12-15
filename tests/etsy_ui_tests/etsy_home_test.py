from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

etsy_page = "https://www.etsy.com"
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
driver.maximize_window()
driver.get(etsy_page)
