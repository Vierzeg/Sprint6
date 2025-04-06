# about_rent_page.py
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.about_rent_locators import *
from helpers.base_text_holders import *
import time

class FillingFieldRent:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнение поля 'Дата'")
    def filling_date_filed(self, date):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(DATE_FIELD_LOCATOR)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((date)))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(date)).click()

    @allure.step("Выбор срока аренды")
    def choose_rent_period(self, rent_period):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RENTAL_PERIOD_LOCATOR)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((rent_period)))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(rent_period)).click()

    @allure.step("Выбор цвета самоката")
    def choose_color_scooter(self, color_scooter):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(color_scooter)).click()

    @allure.step("Пишем комментарий")
    def filling_comment_field(self, comment):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(COMMENT_FIELD_LOCATOR)).send_keys(comment)

    @allure.step("Нажимаем кнопку 'Заказать'")
    def click_order_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ORDER_BUTTON_LOCATOR)
        ).click()

    @allure.step("Нажимаем кнопку 'Да'")
    def click_yes_button(self):
        # Ожидаем, пока элемент станет видимым и кликаем по нему
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CONFIRM_YES_BUTTON_LOCATOR))
        self.driver.find_element(*CONFIRM_YES_BUTTON_LOCATOR).click()
        # WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(CONFIRM_YES_BUTTON_LOCATOR)
        # ).click()

    @allure.step("Проверка что появляетс модальное окно с текстом 'Заказ оформлен'")
    def check_text_order_complete(self, expected_text):
        # Ждем появления модального окна
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ORDER_HEADER_MODAL_LOCATOR)  # Локатор модального окна
        )

        # Используем XPath с contains для поиска текста в модальном окне
        modal_text = self.driver.find_element(
            By.XPATH, f"//*[contains(text(), '{expected_text}')]"  # Проверка, что текст содержится в элементе
        ).text

        # Проверяем, что текст совпадает с ожидаемым
        assert expected_text in modal_text, f"Ожидаемый текст: '{expected_text}', но найден: '{modal_text}'"


    @allure.step("Ожидаем загрузки страницы 'Про аренду'")
    def wait_rent_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ORDER_HEADER_LOCATOR))

    @allure.step("Ожидаем загрузки модального окна 'Хотите оформить заказ?'")
    def wait_confirm_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(WINDOW_CONF_ORDER))


