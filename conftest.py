import pytest
from selenium import webdriver
from data import Url
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def driver():
    firefox_options = Options()
    firefox_options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=firefox_options)
    driver.get(Url.YANDEX_SCOOTER_URL)
    yield driver
    driver.quit()