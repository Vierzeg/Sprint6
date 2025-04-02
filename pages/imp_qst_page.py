# imp_qst_page.py

from locators.imp_qst_locators import QUESTION_LOCATORS, TEXT_LOCATORS
from locators.base_page_locators import *
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageImportantQuestion:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Закрытие окна с cookie")
    def close_cookie_banner(self):
        try:
            # Ожидаем появления баннера с cookies
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(COOKIE_BANNER_LOC)
            )
            # Ожидаем, пока кнопка закрытия станет кликабельной
            cookie_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(COOKIE_BUTTON_LOC)
            )
            # Кликаем по кнопке закрытия баннера с cookies
            cookie_button.click()
            print("Баннер с cookies успешно закрыт.")

        except Exception as e:
            # В случае ошибки выводим сообщение
            print(f"Не удалось закрыть баннер cookie: {e}")

    @allure.step("Клик на вопрос")
    def click_list_button(self, question_locator):
        # Ожидаем, пока элемент не станет кликабельным
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(question_locator)
        )
        self.driver.find_element(*question_locator).click()

    @allure.step("Проверка текста в ответе на вопрос")
    def check_list_text(self, question_locator, expected_text):
        index = QUESTION_LOCATORS.index(question_locator)
        text_locator = TEXT_LOCATORS[index]

        # Ждем, пока текст появится в элементе
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(text_locator, expected_text)
        )

        actual_text = self.driver.find_element(*text_locator).text
        assert actual_text == expected_text, f"Ожидалось: {expected_text}, но получено: {actual_text}"

    @allure.step("Ожидание загрузки главной страницы")
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(LOGO_HOME_LOC))
