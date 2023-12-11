from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(r"drivers\\chrome-win64\\chrome.exe"))
driver.get('https://www.salesforce.com/')
