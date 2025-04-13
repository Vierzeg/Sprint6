# test_transit_to_dzen.py

from pages.home_landing_page import HomeLandingPage
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.url_holders import *


@allure.title("Проверка перехода на Яндекс Дзен по клику на логотип Яндекса")
class TestTransitToDzen:

    @classmethod
    def setup_class(cls):
        # Устанавливаем опции для Firefox (опционально)
        options = Options()
        options.headless = False  # Установите True, если не хотите открывать окно браузера

        # Инициализация драйвера для Firefox
        cls.driver = webdriver.Firefox(options=options)
        cls.driver.get(url_home)  # Начальная страница
        cls.page_home = HomeLandingPage(cls.driver)

    @allure.step("Кликаем на логотип Яндекса")
    def test_transit_to_dzen(self):
        self.page_home.click_yandex_logo_button()  # Клик по логотипу Яндекса

        # Явное ожидание перехода на страницу Яндекс Дзена
        self.page_home.wait_until_url_to_be(url_dzen)

        # Проверка, что URL открылся правильный
        self.page_home.check_url_dzen(url_dzen)  # Проверка, что открылся правильный URL

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()