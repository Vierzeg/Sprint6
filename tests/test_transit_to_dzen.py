# test_transit_to_dzen.py

# from pages.home_landing_page import HomeLandingPage
# from helpers.url_holders import *
# import allure
# import pytest
# from selenium import webdriver
#
# @allure.title("Проверка перехода на Яндекс Дзен по клику на логотип Яндекса")
# class TestTransitToDzen:
#
#     @classmethod
#     def setup_class(cls):
#         cls.driver = webdriver.Chrome()
#         cls.driver.get(url_home)  # Начальная страница
#         cls.page_home = HomeLandingPage(cls.driver)
#
#     @allure.step("Кликаем на логотип Яндекса")
#     def test_transit_to_dzen(self):
#         self.page_home.click_yandex_logo_button()  # Клик по логотипу Яндекса
#         self.page_home.check_url_dzen(url_dzen)  # Проверка, что открылся правильный URL
#
#     @classmethod
#     def teardown_class(cls):
#         cls.driver.quit()

from pages.home_landing_page import HomeLandingPage
from helpers.url_holders import *
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Проверка перехода на Яндекс Дзен по клику на логотип Яндекса")
class TestTransitToDzen:

    @classmethod
    def setup_class(cls):
        # Устанавливаем опции для Firefox (опционально)
        options = Options()
        options.headless = False  # Установите True, если не хотите открывать окно браузера

        # Указываем путь к geckodriver, если он не в PATH
        geckodriver_path = r"C:\Users\geckodriver\geckodriver.exe"

        # Инициализация драйвера для Firefox
        cls.driver = webdriver.Firefox(service=Service(executable_path=geckodriver_path), options=options)
        cls.driver.get(url_home)  # Начальная страница
        cls.page_home = HomeLandingPage(cls.driver)

    @allure.step("Кликаем на логотип Яндекса")
    def test_transit_to_dzen(self):
        self.page_home.click_yandex_logo_button()  # Клик по логотипу Яндекса

        # Явное ожидание перехода на страницу Яндекс Дзена
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(url_dzen)  # Ожидаем, что URL будет соответствовать ожидаемому
        )

        # Проверка, что URL открылся правильный
        self.page_home.check_url_dzen(url_dzen)  # Проверка, что открылся правильный URL

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

