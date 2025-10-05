import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from locators.order_page_locators import OrderPageLocators
from locators.home_page_locators import HomePageLocators
from pages.order_page import OrderPageScooter
from data import Data

class TestOrderScooter:
    @allure.title('Проверка оформления заказа через главную кнопку "Заказать"')
    @allure.description('Оформляем заказ через главную кнопку "Заказать" и проверям что появилось сообщение об успешном оформлении')
    def test_order_scooter_from_top_button(self, driver):
        order_page = OrderPageScooter(driver)
        order_page.click_on_element(OrderPageLocators.TOP_BUTTON_ORDER_LOCATOR)
        order_page.fill_in_personal_information(Data.name_1, Data.surname_1, Data.address_1, OrderPageLocators.METRO_STATION_1_BUTTON_LOCATOR, Data.phone_1)
        order_page.fill_about_rent(Data.date_1, OrderPageLocators.RENTAL_PERIOD_1_DAY_LOCATOR, OrderPageLocators.BLACK_COLOR_LOCATOR, Data.comment_1)
        order_page.click_on_element(OrderPageLocators.CONFIRMATION_OREDER_BUTTON_LOCATOR)
        assert order_page.wait_visibility_element(OrderPageLocators.SUCCESSFUL_ORDER_MASSEGE_LOCATOR)

    @allure.title('Проверка оформления заказа через нижнюю кнопку "Заказать"')
    @allure.description('Оформляем заказ через нижнюю кнопку "Заказать" и проверям что появилось сообщение об успешном оформлении')
    def test_order_scooter_from_bellow_button(self, driver):
        order_page = OrderPageScooter(driver)
        order_page.scroll_to_element(HomePageLocators.BELOW_ORDER_BUTTON)
        order_page.wait_clickable_element(HomePageLocators.BELOW_ORDER_BUTTON)
        order_page.click_on_element(HomePageLocators.BELOW_ORDER_BUTTON)
        order_page.fill_in_personal_information(Data.name_2, Data.surname_2, Data.address_2, OrderPageLocators.METRO_STATION_2_BUTTON_LOCATOR, Data.phone_2)
        order_page.fill_about_rent(Data.date_2, OrderPageLocators.RENTAL_PERIOD_2_DAY_LOCATOR, OrderPageLocators.GRAY_COLOR_LOCATOR, Data.comment_2)
        order_page.click_on_element(OrderPageLocators.CONFIRMATION_OREDER_BUTTON_LOCATOR)
        assert order_page.wait_visibility_element(OrderPageLocators.SUCCESSFUL_ORDER_MASSEGE_LOCATOR)

    
        
