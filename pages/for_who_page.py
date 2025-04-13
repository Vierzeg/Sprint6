# for_who_page.py

from pages.home_landing_page import *
from pages.base_page import BasePage
from locators.for_who_locators import *
from locators.about_rent_locators import *
class FillingFieldCustomer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполняем поле 'Имя'")
    def fill_name_field(self, name):
        self.send_keys(NAME_FIELD_LOCATOR, name)

    @allure.step("Заполняем поле 'Фамилия'")
    def fill_sec_name_field(self, sec_name):
        self.send_keys(SEC_NAME_FIELD_LOCATOR, sec_name)

    @allure.step("Заполняем поле 'Адрес'")
    def fill_address_field(self, address):
        self.send_keys(ADDRESS_FIELD_LOCATOR, address)

    @allure.step("Заполняем поле 'Станция метро'")
    def fill_metro_field(self, metro_st):
        self.send_keys(METRO_FIELD_LOCATOR, metro_st)
        # Дожидаемся появления элементов выпадающего списка
        self.wait_until_visible(CHOOSE_ELEM_LOCATOR)
        option_locator = (
            By.XPATH, f"//*[@id='root']//button[contains(@class, 'select-search__option') and .//div[contains(text(), '{metro_st}')]]"
        )
        self.click(option_locator)

    @allure.step("Заполняем поле 'Телефон'")
    def fill_tel_field(self, telephone_numb):
        self.send_keys(TEL_FIELD_LOCATOR, telephone_numb)

    @allure.step("Нажимаем кнопку 'Далее'")
    def click_next_button(self):
        self.click(NEXT_BUTTON_LOCATOR)

    @allure.step("Ожидание загрузки главной страницы")
    def wait_for_load_whom_page(self):
        self.wait_until_visible(HEADLINE_FOR_WHO_LOCATOR)