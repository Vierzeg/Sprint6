# for_who_page.py

from locators.for_who_locators import *
from helpers.customer_data_holders import *
from pages.home_landing_page import *
from locators.base_page_locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FillingFieldCustomer:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполняем поле 'Имя'")
    def fill_name_field(self, name):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(NAME_FIELD_LOCATOR)).send_keys(name)

    @allure.step("Заполняем поле 'Фамилия'")
    def fill_sec_name_field(self, sec_name):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(SEC_NAME_FIELD_LOCATOR)).send_keys(sec_name)

    @allure.step("Заполняем поле 'Адрес'")
    def fill_address_field(self, address):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ADDRESS_FIELD_LOCATOR)).send_keys(address)

    @allure.step("Заполняем поле 'Станция метро'")
    def fill_metro_field(self, metro_st):
        # Вводим текст в поле
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(METRO_FIELD_LOCATOR)).send_keys(metro_st)

        # Дожидаемся появления элементов выпадающего списка
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (CHOOSE_ELEM_LOCATOR))
        )

        option_locator = (
            By.XPATH, f"//*[@id='root']/div/div[2]/div[2]/div[4]//div[contains(text(), '{metro_st}')]"
        )
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(option_locator)).click()

    @allure.step("Заполняем поле 'Телефон'")
    def fill_tel_field(self, telephone_numb):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(TEL_FIELD_LOCATOR)).send_keys(telephone_numb)


    @allure.step("Нажимаем кнопку 'Далее'")
    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(NEXT_BUTTON_LOCATOR)
        ).click()

    @allure.step("Ожидание загрузки главной страницы")
    def wait_for_load_whom_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HEADLINE_FOR_WHO_LOCATOR))
