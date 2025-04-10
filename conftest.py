# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from helpers.url_holders import *

@pytest.fixture(scope="session")
def browser():
    options = Options()
    options.headless = False  # Установите True, если не хотите открывать окно браузера

    # Создаем экземпляр Firefox WebDriver
    driver = webdriver.Firefox(options=options)
    driver.get(url_home)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def browser():
    """Фикстура для запуска нового экземпляра браузера для каждого теста."""
    options = Options()
    options.headless = False  # Установите True, если не хотите открывать окно браузера

    # Создаем экземпляр Firefox WebDriver
    driver = webdriver.Firefox(options=options)
    driver.get(url_home)

    yield driver  # Возвращаем драйвер для использования в тестах

    driver.quit()  # Закрываем драйвер после завершения теста