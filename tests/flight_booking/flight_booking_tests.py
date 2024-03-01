import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
driver.maximize_window()


def oneway_flight_test():
    driver.get('https://www.travelocity.com/Flights')
    driver.implicitly_wait(5)
    # wait = EC.presence_of_element_located(By.XPATH, "//a/span[@class='uitk-tab-text'][contains(text(),'Roundtrip')]")
    wait = WebDriverWait(driver, 5)
    wait.until(ec.element_to_be_clickable([By.XPATH, "//a/span[@class='uitk-tab-text'][contains(text(),'Roundtrip')]"]))
    print('Web Title: ', driver.title)
    print('Current Website URL: ', driver.current_url)
    wait()
    time.sleep(5)
    driver.find_element(By.ID, 'typeahead-originInput-0').clear()
    time.sleep(5)
    driver.find_element(By.ID, 'typeahead-originInput-0').send_keys('SFO')
    time.sleep(2)
    driver.find_element((By.XPATH, '//*[@data-stid="origin_select-results"]/li[1]')).click()
    time.sleep(2)
    # Here we automate return flight
    # driver.find_element(By.XPATH, 'aria-label="Going to"').click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, '//*[@id="origin_select"]').clear()
    # driver.find_element(By.XPATH, '//*[@id="origin_select"]').send_keys('JFK')
    # time.sleep(2)
    # driver.find_element(By.XPATH, '//*[@data-stid="destination_select-results"]/li[1]').click()
    # time.sleep(2)
    # Here click on search
    # driver.find_element(By.ID, 'search_button').click()
    # time.sleep(5)
    # driver.quit()


if __name__ == '__main__':
    oneway_flight_test()
