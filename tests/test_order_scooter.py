# test_order_scooter.py

import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from pages.for_who_page import FillingFieldCustomer
from pages.about_rent_page import FillingFieldRent
from pages.home_landing_page import HomeLandingPage
from helpers.url_holders import *
from helpers.customer_data_holders import *
from locators.about_rent_locators import *
from helpers.base_text_holders import *


geckodriver_path = r"C:\Users\geckodriver\geckodriver.exe"  # Замените на свой путь
@allure.title("Проверка позитивного флоу заказа самоката")
@allure.description("Тестирование 2-х входов в сценарий заказа самоката")
class TestOrderScooter:

    @allure.step("Сценарий 1: Заказ для CUSTOMER1")
    @pytest.mark.parametrize("customer_data, about_rent", [(CUSTOMER1_DATA, ABOUT_RENT1)])
    def test_scenario_1(self, customer_data, about_rent):
        # Настроим опции для Firefox
        options = Options()
        options.headless = False  # Установите True, если не хотите открывать окно браузера

        # Инициализация драйвера для Firefox
        driver = webdriver.Firefox(service=Service(executable_path=r"C:\Users\geckodriver\geckodriver.exe"), options=options)
        driver.get(url_home)

        # Создание объектов для разных страниц
        home_page = HomeLandingPage(driver)
        customer_page = FillingFieldCustomer(driver)
        rent_page = FillingFieldRent(driver)

        # Получение данных для CUSTOMER1
        name = customer_data[0].get('name_1')
        sec_name = customer_data[1].get('sec_name_1')
        address = customer_data[2].get('address_1')
        metro_st = customer_data[3].get('metro_st_1')
        telephone_numb = customer_data[4].get('telephone_numb_1')

        # Шаги сценария 1
        home_page.wait_for_load_main_page()
        home_page.click_order_button_small()
        customer_page.wait_for_load_whom_page()
        customer_page.fill_name_field(name)
        customer_page.fill_sec_name_field(sec_name)
        customer_page.fill_address_field(address)
        customer_page.fill_metro_field(metro_st)
        customer_page.fill_tel_field(telephone_numb)
        customer_page.click_next_button()
        # Переход на страницу аренды и заполняем её
        rent_page.wait_rent_page()
        rent_page.filling_date_filed(DATE_ELEVEN_LOCATOR)
        rent_page.choose_rent_period(OPTION_THREE_LOCATOR)
        rent_page.choose_color_scooter(GREY_CHECKBOX_LOCATOR)
        rent_page.filling_comment_field(ABOUT_RENT1[0]['comment_1'])
        rent_page.click_order_button()
        rent_page.wait_confirm_page()
        time.sleep(3)
        rent_page.click_yes_button()

        rent_page.check_text_order_complete(text_order_complete)

        # Подтверждение заказа
        driver.quit()  # Закрытие драйвера после завершения теста

    @allure.step("Сценарий 2: Заказ для CUSTOMER2")
    @pytest.mark.parametrize("customer_data, about_rent", [(CUSTOMER2_DATA, ABOUT_RENT2)])
    def test_scenario_2(self, customer_data, about_rent):
        # Настроим опции для Firefox
        options = Options()
        options.headless = False  # Установите True, если не хотите открывать окно браузера

        # Инициализация драйвера для Firefox
        driver = webdriver.Firefox(service=Service(executable_path=r"C:\Users\geckodriver\geckodriver.exe"), options=options)
        driver.get(url_home)

        # Создание объектов для разных страниц
        home_page = HomeLandingPage(driver)
        customer_page = FillingFieldCustomer(driver)
        rent_page = FillingFieldRent(driver)

        # Получение данных для CUSTOMER2
        name = customer_data[0].get('name_2')
        sec_name = customer_data[1].get('sec_name_2')
        address = customer_data[2].get('address_2')
        metro_st = customer_data[3].get('metro_st_2')
        telephone_numb = customer_data[4].get('telephone_numb_2')

        # Шаги сценария 2
        home_page.wait_for_load_main_page()
        home_page.click_order_button_big()
        customer_page.wait_for_load_whom_page()
        customer_page.fill_name_field(name)
        customer_page.fill_sec_name_field(sec_name)
        customer_page.fill_address_field(address)
        customer_page.fill_metro_field(metro_st)
        customer_page.fill_tel_field(telephone_numb)
        customer_page.click_next_button()
        # Переход на страницу аренды и заполняем её
        rent_page.wait_rent_page()
        rent_page.filling_date_filed(DATE_FOURTEEN_LOCATOR)
        rent_page.choose_rent_period(OPTION_FIVE_LOCATOR)
        rent_page.choose_color_scooter(BLACK_PEARL_CHECKBOX_LOCATOR)
        rent_page.filling_comment_field(ABOUT_RENT2[0]['comment_2'])
        rent_page.click_order_button()
        rent_page.wait_confirm_page()
        time.sleep(3)
        rent_page.click_yes_button()

        rent_page.check_text_order_complete(text_order_complete)

        # Подтверждение заказа
        driver.quit()  # Закрытие драйвера после завершения теста
