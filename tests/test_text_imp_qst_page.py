# test_text_imp_qst_page.py

# import pytest
# import allure
# from selenium import webdriver
# from helpers.url_holders import url_home
# from pages.imp_qst_page import PageImportantQuestion
# from helpers.question_text_holders import *
# from locators.imp_qst_locators import QUESTION_LOCATORS
#
# # Параметризуем тесты, используя и локаторы, и текст для проверки
# @allure.title("Проверка текста на важные вопросы")
# @allure.description("Тестирование текста, отображаемого при клике на вопросы")
# @pytest.mark.parametrize("question_locator, expected_text", [
#     (QUESTION_LOCATORS[0], text_qst1),
#     (QUESTION_LOCATORS[1], text_qst2),
#     (QUESTION_LOCATORS[2], text_qst3),
#     (QUESTION_LOCATORS[3], text_qst4),
#     (QUESTION_LOCATORS[4], text_qst5),
#     (QUESTION_LOCATORS[5], text_qst6),
#     (QUESTION_LOCATORS[6], text_qst7),
#     (QUESTION_LOCATORS[7], text_qst8),
# ])
# class TestListQuestion:
#     @classmethod
#     def setup_class(cls):
#         cls.driver = webdriver.Chrome()
#         cls.driver.get(url_home)
#         cls.qst_of_list = PageImportantQuestion(cls.driver)
#         cls.qst_of_list.close_cookie_banner()
#
#     @allure.step("Клик на вопрос и проверка текста")
#     def test_text_list_question(self, browser, question_locator, expected_text):
#         self.qst_of_list.wait_for_load_home_page()
#         self.qst_of_list.click_list_button(question_locator)
#         self.qst_of_list.check_list_text(question_locator, expected_text)
#
#
#     @classmethod
#     def teardown_class(cls):
#         cls.driver.quit()

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from helpers.url_holders import url_home
from pages.imp_qst_page import PageImportantQuestion
from helpers.question_text_holders import *
from locators.imp_qst_locators import QUESTION_LOCATORS

# Параметризуем тесты, используя и локаторы, и текст для проверки
@allure.title("Проверка текста на важные вопросы")
@allure.description("Тестирование текста, отображаемого при клике на вопросы")
@pytest.mark.parametrize("question_locator, expected_text", [
    (QUESTION_LOCATORS[0], text_qst1),
    (QUESTION_LOCATORS[1], text_qst2),
    (QUESTION_LOCATORS[2], text_qst3),
    (QUESTION_LOCATORS[3], text_qst4),
    (QUESTION_LOCATORS[4], text_qst5),
    (QUESTION_LOCATORS[5], text_qst6),
    (QUESTION_LOCATORS[6], text_qst7),
    (QUESTION_LOCATORS[7], text_qst8),
])
class TestListQuestion:
    @classmethod
    def setup_class(cls):
        # Устанавливаем опции для Firefox (опционально)
        options = Options()
        options.headless = False  # Установите True, если не хотите открывать окно браузера

        # Указываем путь к geckodriver, если он не в PATH
        geckodriver_path = r"C:\Users\geckodriver\geckodriver.exe"  # Замените на путь к вашему geckodriver

        # Инициализация драйвера для Firefox
        cls.driver = webdriver.Firefox(service=Service(executable_path=geckodriver_path), options=options)
        cls.driver.get(url_home)
        cls.qst_of_list = PageImportantQuestion(cls.driver)
        cls.qst_of_list.close_cookie_banner()

    @allure.step("Клик на вопрос и проверка текста")
    def test_text_list_question(self, browser, question_locator, expected_text):
        self.qst_of_list.wait_for_load_home_page()
        self.qst_of_list.click_list_button(question_locator)
        self.qst_of_list.check_list_text(question_locator, expected_text)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
