'''
Created on 21-Oct-2019

@author: hemasunder.g
'''

from Utilities import utilities as utils
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type browser name eg: chrome or ie")

@pytest.yield_fixture(scope="function")
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=utils.chromepath)
    elif browser == 'ie':
        driver = webdriver.Ie(executable_path=utils.iepath)
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    request.cls.driver = driver
    driver.get(utils.url)
    yield
#     driver.quit()