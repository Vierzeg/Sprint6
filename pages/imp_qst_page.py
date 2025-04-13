# imp_qst_page.py

import allure
from pages.base_page import BasePage
from locators.base_page_locators import *
from locators.imp_qst_locators import *

class PageImportantQuestion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Закрытие окна с cookie")
    def close_cookie_banner(self):
        self.wait_until_visible(COOKIE_BANNER_LOC)
        self.click(COOKIE_BUTTON_LOC)

    @allure.step("Клик на вопрос")
    def click_list_button(self, question_locator):
        self.click(question_locator)

    @allure.step("Проверка текста в ответе на вопрос")
    def check_list_text(self, question_locator, expected_text):
        index = QUESTION_LOCATORS.index(question_locator)
        text_locator = TEXT_LOCATORS[index]

        # Ждем, пока текст появится в элементе
        self.wait_until_text_present_in_element(text_locator, expected_text)
        actual_text = self.find_element(text_locator).text
        assert actual_text == expected_text, f"Ожидалось: {expected_text}, но получено: {actual_text}"

    @allure.step("Ожидание загрузки главной страницы")
    def wait_for_load_home_page(self):
        self.wait_until_visible(LOGO_HOME_LOC)