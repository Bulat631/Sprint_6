from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators

class OrderPageLocators(BasePageLocators):
    NAME_INPUT_LOCATOR = [By.XPATH, "//input[@placeholder='* Имя']"] # поле Имя
    SURNAME_INPUT_LOCATOR = [By.XPATH, "//input[@placeholder='* Фамилия']"] # поле Фамилия
    ADDRESS_INPUT_LOCATOR = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"] # поле Адрес
    METRO_INPUT_LOCATOR = [By.XPATH, "//input[@placeholder='* Станция метро']"] # поле Метро
    METRO_STATION_1_BUTTON_LOCATOR = [By.XPATH, "//li[@class='select-search__row']/button[@value='1']"] #
    METRO_STATION_2_BUTTON_LOCATOR = [By.XPATH, "//li[@class='select-search__row']/button[@value='2']"] #
    PHONE_INPUT_LOCATOR = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"] # поле Телефон
    FUTHER_BUTTON_LOCATOR = [By.XPATH, "//div[@class='Order_NextButton__1_rCA']/button"] # кнопка Далее
    DATE_INPUT_LOCATOR = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"] # поле Когда привезти самокат
    RESULTING_DAY_LOCATOR = [By.XPATH, "//div[@class='react-datepicker__month']//div[contains(@class, '--selected')]"]
    PERIOD_FIELD_LOCATOR = [By.XPATH, "//div[@class='Dropdown-root']"] # поле выбора срока аренды самоката
    RENTAL_PERIOD_1_DAY_LOCATOR = [By.XPATH, "//div[text()='сутки']"] # кнопка выбора срока на сутки
    RENTAL_PERIOD_2_DAY_LOCATOR = [By.XPATH, "//div[text()='двое суток']"] # кнопка выбора срока на 2 суток
    BLACK_COLOR_LOCATOR = [By.XPATH, "//label[text()='чёрный жемчуг']"] # чекбокс черного самоката
    GRAY_COLOR_LOCATOR = [By.XPATH, "//label[text()='серая безысходность']"] # чекбокс серого самоката
    COMMENT_INPUT_LOCATOR = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"] # поле Комментария
    ORDER_BUTTON_SCOOTER_LOCATOR = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"] # кнопка завершения заказа самоката
    CONFIRMATION_OREDER_BUTTON_LOCATOR = [By.XPATH, "//button[text()='Да']"] # кнопка подтверждение заказа
    SUCCESSFUL_ORDER_MASSEGE_LOCATOR = [By.XPATH, "//div[text()='Заказ оформлен']"] # сообщение об успешном заказе
