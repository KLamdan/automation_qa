import pytest
from selenium import webdriver
from selenium.webdriver.chromium.webdriver import ChromiumDriver


@pytest.fixture()
def driver() -> ChromiumDriver:
	chrome_driver = webdriver.Chrome()
	chrome_driver.maximize_window()
	yield chrome_driver
	chrome_driver.quit()
