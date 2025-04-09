# conftest.py

import pytest
from selenium import webdriver
from helpers.url_holders import url_home
from pages.imp_qst_page import PageImportantQuestion
from selenium.webdriver.firefox.options import Options

# @pytest.fixture(scope="function")
# def browser():
#     driver = webdriver.Chrome()
#     driver.get(url_home)
#     qst_of_list = PageImportantQuestion(driver)
#     qst_of_list.close_cookie_banner()
#     yield qst_of_list
#     driver.quit()
#
# @pytest.fixture(scope="session")
# def driver():
#     options = Options()
#     options.headless = False  # Устанавливаем в True, если хотите запускать тесты без отображения браузера (headless режим)
#
#     # Создаем экземпляр Firefox WebDriver
#     driver = webdriver.Firefox(options=options)  # Здесь мы используем Firefox вместо Chrome
#     driver.get("https://example.com")  # Открытие страницы для тестов
#     yield driver
#     driver.quit()  # Закрытие браузера после тестов

# import pytest
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from helpers.url_holders import url_home
# from pages.imp_qst_page import PageImportantQuestion
#
# @pytest.fixture(scope="function")
# def browser():
#     options = Options()
#     options.headless = False  # Установите в True для работы без UI
#
#     # Создаем экземпляр Firefox WebDriver
#     driver = webdriver.Firefox(options=options)
#     driver.get(url_home)
#     page = PageImportantQuestion(driver)
#     page.close_cookie_banner()  # Закрытие баннера с куки
#     yield page
#     driver.quit()

# @pytest.fixture(scope="session")
# def driver():
#     options = Options()
#     options.headless = False
#
#     driver = webdriver.Firefox(options=options)
#     driver.get(url_home)  # Открытие домашней страницы
#     yield driver
#     driver.quit()
import pytest
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from helpers.url_holders import url_home
# from pages.imp_qst_page import PageImportantQuestion

# @pytest.fixture(scope="function")
# def browser():
#     options = Options()
#     options.headless = False  # Установите в True для работы без UI
#
#     # Создаем экземпляр Firefox WebDriver
#     driver = webdriver.Firefox(options=options)
#     page = PageImportantQuestion(driver)
#     page.open_url(url_home)  # Открытие домашней страницы
#     page.close_cookie_banner()  # Закрытие баннера с куки
#     yield page
#     driver.quit()
#
# @pytest.fixture(scope="session")
# def driver():
#     options = Options()
#     options.headless = False
#
#     driver = webdriver.Firefox(options=options)
#     driver.get(url_home)  # Открытие домашней страницы
#     yield driver
#     driver.quit()

import pytest
# from selenium import webdriver
# from helpers.url_holders import url_home
# from pages.imp_qst_page import PageImportantQuestion
# from selenium.webdriver.firefox.options import Options

# @pytest.fixture(scope="function")
# def browser():
#     options = Options()
#     options.headless = False
#     driver = webdriver.Firefox(options=options)
#     driver.get(url_home)
#     yield driver
#     driver.quit()
#
# @pytest.fixture(scope="session")
# def driver():
#     options = Options()
#     options.headless = False
#     driver = webdriver.Firefox(options=options)
#     driver.get(url_home)
#     yield driver
#     driver.quit()

# import pytest
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from helpers.url_holders import *
#
# @pytest.fixture(scope="function")
# def browser():
#     # Инициализация драйвера для Firefox
#     options = Options()
#     options.headless = False  # Установите True, если не хотите открывать окно браузера
#     driver = webdriver.Firefox(options=options)
#     driver.get(url_home)
#     yield driver
#     driver.quit()
#
# @pytest.fixture(scope="session")
# def driver():
#     # Инициализация драйвера для Firefox
#     options = Options()
#     options.headless = False  # Установите True, если не хотите открывать окно браузера
#     driver = webdriver.Firefox(options=options)
#     driver.get(url_home)
#     yield driver
#     driver.quit()
#

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from helpers.url_holders import url_home
from helpers.question_text_holders import *
from helpers.url_holders import *
from helpers.base_text_holders import *
from helpers.customer_data_holders import *
from locators.base_page_locators import *
from locators.imp_qst_locators import *
from locators.for_who_locators import *
from locators.about_rent_locators import *

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