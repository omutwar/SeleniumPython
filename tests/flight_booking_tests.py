import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

from utils.config_reader import ConfigReader

driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.maximize_window()

test_site = ConfigReader.get_property('sites', 'velocityURL')


def oneway_trip_test():
    """ Open the web application """

    driver.get(test_site)
    driver.implicitly_wait(5)

    locator = (By.XPATH, "//a/span[@class='uitk-tab-text'][contains(text(),'Roundtrip')]")
    is_element_clickable = wait.until(ec.element_to_be_clickable(locator))
    print(is_element_clickable)
    print('Web Title: ', driver.title)
    print('Current Website URL: ', driver.current_url)

    driver.find_element(By.CSS_SELECTOR, "button[aria-label='Leaving from']").send_keys("SFO")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button[aria-label='Going to']").send_keys('LAX')
    time.sleep(2)
    driver.find_element((By.CSS_SELECTOR, "#date_form_field-btn")).click()
    time.sleep(2)


def round_trip_test():
    """ Open the web application """
    driver.get(test_site)
    driver.implicitly_wait(5)

    driver.find_element(By.XPATH, 'aria-label="Going to"').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="origin_select"]').clear()
    driver.find_element(By.XPATH, '//*[@id="origin_select"]').send_keys('JFK')
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@data-stid="destination_select-results"]/li[1]').click()
    time.sleep(2)
    # Here click on search
    driver.find_element(By.ID, 'search_button').click()
    time.sleep(5)
    driver.quit()

# if __name__ == '__main__':
#     oneway_trip_test()
#     round_trip_test()
