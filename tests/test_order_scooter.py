import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from locators.order_page_locators import OrderPageLocators
from locators.home_page_locators import HomePageLocators
from pages.order_page import OrderPageScooter
from pages.home_page import HomePageScooter
from data import UsersData

class TestOrderScooter:
    @allure.title('Проверка оформления заказа через главную кнопку "Заказать"')
    @allure.description('Оформляем заказ через главную кнопку "Заказать" и проверям что появилось сообщение об успешном оформлении')
    def test_order_scooter_from_top_button(self, driver):
        home_page = HomePageScooter(driver)
        order_page = OrderPageScooter(driver)
        home_page.click_to_top_button_order()
        order_page.fill_in_personal_information(UsersData.name_1, UsersData.surname_1, UsersData.address_1, OrderPageLocators.METRO_STATION_1_BUTTON_LOCATOR, UsersData.phone_1)
        order_page.fill_about_rent(UsersData.date_1, OrderPageLocators.RENTAL_PERIOD_1_DAY_LOCATOR, OrderPageLocators.BLACK_COLOR_LOCATOR, UsersData.comment_1)
        order_page.click_to_button_order_confirmation()
        assert order_page.wait_visibility_element(OrderPageLocators.SUCCESSFUL_ORDER_MASSEGE_LOCATOR)

    @allure.title('Проверка оформления заказа через нижнюю кнопку "Заказать"')
    @allure.description('Оформляем заказ через нижнюю кнопку "Заказать" и проверям что появилось сообщение об успешном оформлении')
    def test_order_scooter_from_bellow_button(self, driver):
        home_page = HomePageScooter(driver)
        order_page = OrderPageScooter(driver)
        home_page.scroll_and_click_below_order_button()
        order_page.fill_in_personal_information(UsersData.name_2, UsersData.surname_2, UsersData.address_2, OrderPageLocators.METRO_STATION_2_BUTTON_LOCATOR, UsersData.phone_2)
        order_page.fill_about_rent(UsersData.date_2, OrderPageLocators.RENTAL_PERIOD_2_DAY_LOCATOR, OrderPageLocators.GRAY_COLOR_LOCATOR, UsersData.comment_2)
        order_page.click_to_button_order_confirmation()
        assert order_page.wait_visibility_element(OrderPageLocators.SUCCESSFUL_ORDER_MASSEGE_LOCATOR)

    
        
