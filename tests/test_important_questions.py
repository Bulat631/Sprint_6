import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePageScooter
from data import Data

class TestImportantQuestions:
    @allure.title('Проверка текстов в блоке "Вопросы о важном"')
    @allure.description('Кликаем на соответствующий вопрос и проверяем что отобразившийся текст соответствует text_question')
    @pytest.mark.parametrize(
        'question_locator, answer_locator, text_question',
        [
            [HomePageLocators.QUESTION_1_LOCATOR, HomePageLocators.ANSWER_1_LOCATOR, Data.text_1_question],
            [HomePageLocators.QUESTION_2_LOCATOR, HomePageLocators.ANSWER_2_LOCATOR, Data.text_2_question],
            [HomePageLocators.QUESTION_3_LOCATOR, HomePageLocators.ANSWER_3_LOCATOR, Data.text_3_question],
            [HomePageLocators.QUESTION_4_LOCATOR, HomePageLocators.ANSWER_4_LOCATOR, Data.text_4_question],
            [HomePageLocators.QUESTION_5_LOCATOR, HomePageLocators.ANSWER_5_LOCATOR, Data.text_5_question],
            [HomePageLocators.QUESTION_6_LOCATOR, HomePageLocators.ANSWER_6_LOCATOR, Data.text_6_question],
            [HomePageLocators.QUESTION_7_LOCATOR, HomePageLocators.ANSWER_7_LOCATOR, Data.text_7_question],
            [HomePageLocators.QUESTION_8_LOCATOR, HomePageLocators.ANSWER_8_LOCATOR, Data.text_8_question]
        ]
    )
    def test_important_questions(self, driver, question_locator, answer_locator, text_question):
        home_page = HomePageScooter(driver)
        home_page.scroll_to_questions()
        home_page.wait_clickable_element(question_locator)
        home_page.click_on_element(question_locator)
        text_element = home_page.get_element_text(answer_locator)
        assert text_element == text_question

