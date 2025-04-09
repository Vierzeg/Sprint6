# base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_until_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_until_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_until_presence(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait_until_clickable(locator)
        self.find_element(locator).click()

    def send_keys(self, locator, value):
        self.wait_until_visible(locator)
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(value)

    # Новый метод для ожидания появления текста в элементе
    def wait_until_text_present_in_element(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))