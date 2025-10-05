from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGO_YANDEX_LOCATOR = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI'] # логотип Яндекса
    LOGO_SCOOTER_LOCATOR = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR'] # логотип Самоката
    TOP_BUTTON_ORDER_LOCATOR = [By.CLASS_NAME, 'Button_Button__ra12g'] # верхняя кнопка заказа самоката