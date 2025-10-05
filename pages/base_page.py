import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.firefox.webdriver import WebDriver

class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_new_window(self):    
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_visibility_element(self, locator):
        return WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(locator))
    
    def wait_clickable_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text
    
    def wait_url(self, url):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))