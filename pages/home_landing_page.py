# home_landing_page.py

import allure
from pages.base_page import BasePage
from locators.base_page_locators import *

class HomeLandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по кнопке 'Заказать' в шапке страницы")
    def click_order_button_small(self):
        self.click(ORDER_BUTTON_SMALL)

    @allure.step("Клик по кнопке 'Заказать' внизу страницы")
    def click_order_button_big(self):
        element = self.find_element(ORDER_BUTTON_BIG)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.click(ORDER_BUTTON_BIG)

    @allure.step("Клик по кнопке 'Самокат' в логотипе")
    def click_logo_scooter_button(self):
        self.click(LOGO_SCOOTER_BUTTON)

    @allure.step("Проверка что после клика по кнопке 'Самокат' перешли на главную страницу")
    def check_url_home_scooter(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Ожидаемый URL {expected_url}, но текущий {current_url}"

    @allure.step("Кликаем на кнопку 'Яндекс' в логотипе")
    def click_yandex_logo_button(self):
        self.click(LOGO_YANDEX_BUTTON)
        self.wait_for_number_of_windows_to_be(2)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    @allure.step("Проверка, что открылась страница Яндекс Дзена")
    def check_url_dzen(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, но текущий: {current_url}"

    @allure.step("Ожидание загрузки главной страницы")
    def wait_for_load_main_page(self):
        self.wait_until_visible(LOGO_HOME_LOC)
