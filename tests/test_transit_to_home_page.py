# test_transit_to_home_page.py

from pages.home_landing_page import *
from helpers.url_holders import *
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

@allure.title("Проверка кнопки 'Самокат' в логотипе")

class TestTransitToHome:

    @classmethod
    def setup_class(cls):
        # Устанавливаем опции для Firefox (опционально)
        options = Options()
        options.headless = False  # Установите True, если не хотите открывать окно браузера

        # Указываем путь к geckodriver, если он не в PATH
        geckodriver_path = r"C:\Users\geckodriver\geckodriver.exe"

        # Инициализация драйвера для Firefox
        cls.driver = webdriver.Firefox(service=Service(executable_path=geckodriver_path), options=options)
        cls.driver.get(url_home)
        cls.page_home = HomeLandingPage(cls.driver)

    @allure.step("Кликаем на кнопку 'Заказать'")
    def test_transit_to_home(self):
        self.page_home.click_order_button_small()  # Клик по кнопке "Заказать" (маленькая)
        self.page_home.click_logo_scooter_button()  # Клик по логотипу "Самокат"

        # Теперь проверим, что URL страницы соответствует ожидаемому
        self.page_home.check_url_home_scooter(url_home)  # Сравнение текущего URL с ожидаемым

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



