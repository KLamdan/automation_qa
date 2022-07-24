from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_locator_type(locator: str):
	locator = locator.lower()
	locator_list = {
		"css": By.CSS_SELECTOR,
		"xpath": By.XPATH,
		"id": By.ID,
		"name": By.NAME,
		"tag": By.TAG_NAME,
		"lint_text": By.LINK_TEXT,
		"class": By.CLASS_NAME,
		"p_link_text": By.PARTIAL_LINK_TEXT
		
	}
	return locator_list.get(locator)


class BasePage:
	timeout = 100
	base_url = 'https://demoqa.com/'
	
	def __init__(self, driver: webdriver, url: str):
		self.driver: ChromiumDriver = driver
		self.base_url = url if not None else BasePage.base_url
		self.wait = WebDriverWait(self.driver, BasePage.timeout)
	
	def base_page_open(self) -> webdriver:
		self.driver.get(BasePage.base_url)
		return self.driver
	
	def element_is_visible(self, locator_type, locator) -> WebElement:
		loc_type = get_locator_type(locator_type)
		if loc_type is None:
			raise Exception("Sorry, Locator type not found")
		return self.wait.until(EC.visibility_of_element_located((get_locator_type(locator_type), locator)))
	
	def elements_are_visible(self, locator_type: str, locator: str) -> [WebElement]:
		loc_type = get_locator_type(locator_type)
		if loc_type is None:
			raise Exception("Sorry, Locator type not found")
		return self.wait.until(EC.visibility_of_all_elements_located((loc_type, locator)))
	
	def element_is_present(self, locator_type, locator) -> WebElement:
		loc_type = get_locator_type(locator_type)
		if loc_type is None:
			raise Exception("Sorry, Locator type not found")
		return self.wait.until(EC.presence_of_element_located((loc_type, locator)))
	
	def elements_are_presents(self, locator_type: str, locator: str) -> [WebElement]:
		loc_type = get_locator_type(locator_type)
		if loc_type is None:
			raise Exception("Sorry, Locator type not found")
		print(f"SELECTOR = {loc_type}")
		elements: [WebElement] = self.wait.until(EC.presence_of_all_elements_located((loc_type, locator)))
		print(elements)
		return elements
	
	def find_element_by_text(self, tag: str, text: str) -> WebElement:
		elements = self.driver.find_elements(By.TAG_NAME, tag)
		print(" elements count ".format(len(elements)))
		index = [element.text for element in elements].index("Forms")
		element = elements[index]
		return element
	
	def element_is_clickable(self, locator_type, locator) -> WebElement:
		loc_type = get_locator_type(locator_type)
		if loc_type is None:
			raise Exception("Sorry, Locator type not found")
		return self.wait.until(EC.element_to_be_clickable((loc_type, locator)))
