import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import HomePageLocators
from selenium.webdriver.firefox.webdriver import WebDriver
from pages.base_page import BasePage

class HomePageScooter(BasePage):
    
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    def scroll_to_block_with_questions(self):
        self.scroll_to_element(HomePageLocators.QUESTION_8_LOCATOR)

    def click_to_logo_yandex(self):
        self.click_on_element(HomePageLocators.LOGO_YANDEX_LOCATOR)

    def click_to_logo_scooter(self):
        self.click_on_element(HomePageLocators.LOGO_SCOOTER_LOCATOR)

    def click_to_top_button_order(self):
        self.click_on_element(HomePageLocators.TOP_BUTTON_ORDER_LOCATOR)

    def click_to_below_order_button(self):
        self.click_on_element(HomePageLocators.BELOW_ORDER_BUTTON)
        
    def scroll_to_below_order_button(self):
        self.scroll_to_element(HomePageLocators.BELOW_ORDER_BUTTON)

    def wait_to_clickable_below_order_button(self):
        self.wait_clickable_element(HomePageLocators.BELOW_ORDER_BUTTON)

    def scroll_and_click_below_order_button(self):
        self.scroll_to_element(HomePageLocators.BELOW_ORDER_BUTTON)
        self.wait_clickable_element(HomePageLocators.BELOW_ORDER_BUTTON)
        self.click_on_element(HomePageLocators.BELOW_ORDER_BUTTON)

    