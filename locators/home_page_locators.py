from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators

class HomePageLocators(BasePageLocators):
    BELOW_ORDER_BUTTON = [By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']"] # нижняя кнопка заказа самоката Button_Button__ra12g Button_UltraBig__UU3Lp'
    QUESTION_1_LOCATOR = [By.ID, 'accordion__heading-0'] # первый вопрос
    QUESTION_2_LOCATOR= [By.ID, 'accordion__heading-1'] # второй вопрос
    QUESTION_3_LOCATOR = [By.ID, 'accordion__heading-2'] # третий вопрос
    QUESTION_4_LOCATOR = [By.ID, 'accordion__heading-3'] # четвертый вопрос
    QUESTION_5_LOCATOR = [By.ID, 'accordion__heading-4'] # пятый вопрос
    QUESTION_6_LOCATOR = [By.ID, 'accordion__heading-5'] # шестой вопрос
    QUESTION_7_LOCATOR = [By.ID, 'accordion__heading-6'] # седьмой вопрос
    QUESTION_8_LOCATOR = [By.ID, 'accordion__heading-7'] # восьмой вопрос
    ANSWER_1_LOCATOR = [By.XPATH, "//div[@id='accordion__panel-0']/p"] # 
    ANSWER_2_LOCATOR = [By.XPATH, "//div[@id='accordion__panel-1']/p"] #
    ANSWER_3_LOCATOR = [By.XPATH, "//div[@id='accordion__panel-2']/p"] #
    ANSWER_4_LOCATOR = [By.XPATH, "//div[@id='accordion__panel-3']/p"] # тексты вопросов
    ANSWER_5_LOCATOR = [By.XPATH, "//div[@id='accordion__panel-4']/p"] #
    ANSWER_6_LOCATOR = [By.XPATH, "//div[@id='accordion__panel-5']/p"] #
    ANSWER_7_LOCATOR = [By.XPATH, "//div[@id='accordion__panel-6']/p"] #
    ANSWER_8_LOCATOR = [By.XPATH, "//div[@id='accordion__panel-7']/p"] #