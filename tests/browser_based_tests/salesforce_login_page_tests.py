"""

"""
from selenium import webdriver
import pytest


def inc(num):
    return num + 1


def f():
    raise SystemExit(1)


def test_answer():
    assert inc(3) == 4


def test_mytest():
    with pytest.raises(SystemExit):
        f()


def test_salesforce_login():

    driver = webdriver.Chrome()
    driver.get("https://www.salesforce.com")

    web_title = driver.title
    print(web_title)

    driver.quit()


