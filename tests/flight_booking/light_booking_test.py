from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

gecko = webdriver.Firefox(executable_path='drivers/geckodriver/geckodriver.exe')


def test_oneway_flight():
    gecko.get('https://www.travelocity.com/Flights')
    gecko.maximize_window()
    gecko.implicitly_wait(5)
    # wait = EC.presence_of_element_located(By.XPATH, "//a/span[@class='uitk-tab-text'][contains(text(),'Roundtrip')]")
    wait = WebDriverWait(gecko, 5)
    wait.until(EC.element_to_be_clickable(By.XPATH, "//a/span[@class='uitk-tab-text'][contains(text(),'Roundtrip')]"))
    print('Web Title: ', gecko.title)
    print('Current Website URL: ', gecko.current_url)
    wait()
    time.sleep(5)
    gecko.find_element(By.ID, 'typeahead-originInput-0').clear()
    time.sleep(5)
    gecko.find_element(By.ID, 'typeahead-originInput-0').send_keys('SFO')
    time.sleep(2)
    gecko.find_element((By.XPATH, '//*[@data-stid="origin_select-results"]/li[1]')).click()
    time.sleep(2)
    # Here we automate return flight
    # gecko.find_element(By.XPATH, 'aria-label="Going to"').click()
    # time.sleep(2)
    # gecko.find_element(By.XPATH, '//*[@id="origin_select"]').clear()
    # gecko.find_element(By.XPATH, '//*[@id="origin_select"]').send_keys('JFK')
    # time.sleep(2)
    # gecko.find_element(By.XPATH, '//*[@data-stid="destination_select-results"]/li[1]').click()
    # time.sleep(2)
    # Here click on search
    # gecko.find_element(By.ID, 'search_button').click()
    # time.sleep(5)
    # gecko.quit()
