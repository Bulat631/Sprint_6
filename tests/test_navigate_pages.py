import pytest
import allure
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePageScooter
from data import Url

class TestNavigatePages:
    @allure.title('Проверка клика на логотип Самоката')
    @allure.description('Кликаем на логотип Самоката и проверяем, что загрузился URL главной страницы')
    def test_navigate_from_button_scooter(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_to_top_button_order()
        home_page.click_to_logo_scooter()
        assert home_page.wait_url(Url.YANDEX_SCOOTER_URL)

    @allure.title('Проверка клика на логотип Яндекса')
    @allure.description('Кликаем на логотип Яндекса и проверяем, что загрузился URL страницы Дзена')
    def test_navigate_from_button_yandex(self, driver):
        home_page = HomePageScooter(driver)
        home_page.click_to_logo_yandex()
        home_page.switch_to_new_window()
        assert home_page.wait_url(Url.DZEN_URL)

    