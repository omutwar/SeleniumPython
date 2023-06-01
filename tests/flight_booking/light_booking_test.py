from selenium import webdriver
import time
from selenium.webdriver.common.by import By

gecho = webdriver.firefox


def test_oneway_flight():
    gecho.get('https://www.travelocity.com/Flights')
    time.sleep(5)
    gecho.quit()
