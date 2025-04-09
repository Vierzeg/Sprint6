# about_rent_page.py

import allure
from pages.base_page import BasePage
from locators.about_rent_locators import *
from selenium.webdriver.common.by import By
class FillingFieldRent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнение поля 'Дата'")
    def filling_date_filed(self, date):
        self.click(DATE_FIELD_LOCATOR)
        self.wait_until_visible(date)
        self.click(date)

    @allure.step("Выбор срока аренды")
    def choose_rent_period(self, rent_period):
        self.click(RENTAL_PERIOD_LOCATOR)
        self.wait_until_visible(rent_period)
        self.click(rent_period)

    @allure.step("Выбор цвета самоката")
    def choose_color_scooter(self, color_scooter):
        self.click(color_scooter)

    @allure.step("Пишем комментарий")
    def filling_comment_field(self, comment):
        self.send_keys(COMMENT_FIELD_LOCATOR, comment)

    @allure.step("Нажимаем кнопку 'Заказать'")
    def click_order_button(self):
        self.click(ORDER_BUTTON_LOCATOR)

    @allure.step("Нажимаем кнопку 'Да'")
    def click_yes_button(self):
        self.wait_until_visible(CONFIRM_YES_BUTTON_LOCATOR)
        self.click(CONFIRM_YES_BUTTON_LOCATOR)

    @allure.step("Проверка что появилось модальное окно с текстом 'Заказ оформлен'")
    def check_text_order_complete(self, expected_text):
        self.wait_until_visible(ORDER_HEADER_MODAL_LOCATOR)
        modal_text = self.find_element((By.XPATH, f"//*[contains(text(), '{expected_text}')]")).text
        assert expected_text in modal_text, f"Ожидаемый текст: '{expected_text}', но найден: '{modal_text}'"

    @allure.step("Ожидаем загрузки страницы 'Про аренду'")
    def wait_rent_page(self):
        self.wait_until_visible(ORDER_HEADER_LOCATOR)

    @allure.step("Ожидаем загрузки модального окна 'Хотите оформить заказ?'")
    def wait_confirm_page(self):
        self.wait_until_visible(WINDOW_CONF_ORDER)
