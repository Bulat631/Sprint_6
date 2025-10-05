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
    