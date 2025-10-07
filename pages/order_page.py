import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.firefox.webdriver import WebDriver
from pages.base_page import BasePage

class OrderPageScooter(BasePage):
    
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def set_name(self, name):
        self.search_element(OrderPageLocators.NAME_INPUT_LOCATOR).send_keys(name)

    def set_sername(self, sername):
        self.search_element(OrderPageLocators.SURNAME_INPUT_LOCATOR).send_keys(sername)

    def set_address(self, address):
        self.search_element(OrderPageLocators.ADDRESS_INPUT_LOCATOR).send_keys(address)

    def set_phone(self, phone):
        self.search_element(OrderPageLocators.PHONE_INPUT_LOCATOR).send_keys(phone)

    def fill_in_personal_information(self, name, sername, address, locator_station, phone):
        self.set_name(name)
        self.set_sername(sername)
        self.set_address(address)
        self.click_on_element(OrderPageLocators.METRO_INPUT_LOCATOR)
        self.click_on_element(locator_station)
        self.set_phone(phone)
        self.click_on_element(OrderPageLocators.FUTHER_BUTTON_LOCATOR)

    def set_data(self, data):
        self.search_element(OrderPageLocators.DATE_INPUT_LOCATOR).send_keys(data)

    def set_comment(self, comment):
        self.search_element(OrderPageLocators.COMMENT_INPUT_LOCATOR).send_keys(comment)

    def click_to_button_order_confirmation(self):
        self.click_on_element(OrderPageLocators.CONFIRMATION_OREDER_BUTTON_LOCATOR) 

    def fill_about_rent(self, data, period_locator, color_scooter, comment):
        self.set_data(data)
        self.click_on_element(OrderPageLocators.RESULTING_DAY_LOCATOR)
        self.click_on_element(OrderPageLocators.PERIOD_FIELD_LOCATOR)
        self.click_on_element(period_locator)
        self.click_on_element(color_scooter)
        self.set_comment(comment)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_SCOOTER_LOCATOR)



    