import time
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.Base_page import BasePage


# div.category-cards >"
# /html/body/div[2]/div/div/div[2]/div
#//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[2]/span
def test_base_page(driver: WebDriver, url=""):
	base_page = BasePage(driver, url)
	base_page.base_page_open()
	element = base_page.find_element_by_text('h5', 'Forms')
	assert element is not None
	assert element.text == "Forms"
	element.click()
	form = base_page.element_is_present('xpath', '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/ul/li')
	form.click()
	name = base_page.element_is_visible('css', '#firstName')
	name.send_keys("SAGY")
	time.sleep(10)
	
	

# driver.execute('param[0].click()', form)
