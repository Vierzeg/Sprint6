# base_page.py

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента по локатору")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Ожидание отображения элемента")
    def wait_until_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание пока элемент не станет кликабельным")
    def wait_until_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидание присутствия элемента в DOM")
    def wait_until_presence(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Ожидание, пока URL станет: {expected_url}")
    def wait_until_url_to_be(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))

    @allure.step("Ожидание, пока количество окон не станет: {expected_number}")
    def wait_for_number_of_windows_to_be(self, expected_number, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(expected_number))

    @allure.step("Клик по элементу")
    def click(self, locator):
        self.wait_until_clickable(locator)
        self.find_element(locator).click()

    @allure.step("Ввод текста в поле: {locator}")
    def send_keys(self, locator, value):
        self.wait_until_visible(locator)
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(value)

    @allure.step("Ожидание текста '{text}' в элементе")
    # Новый метод для ожидания появления текста в элементе
    def wait_until_text_present_in_element(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
