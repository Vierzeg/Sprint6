# home_landing_page.py
import allure
from locators.base_page_locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomeLandingPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик по кнопке 'Заказать' в шапке страницы")
    def click_order_button_small(self):
        # Ожидаем, пока элемент не станет кликабельным
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ORDER_BUTTON_SMALL)
        )
        self.driver.find_element(*ORDER_BUTTON_SMALL).click()

    @allure.step("Клик по кнопке 'Заказать' внизу страницы")
    def click_order_button_big(self):
        # Ожидаем, пока элемент не станет кликабельным
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ORDER_BUTTON_BIG)
        )
        self.driver.find_element(*ORDER_BUTTON_BIG).click()


    @allure.step("Клик по кнопке 'Самокат' в логотипе")
    def click_logo_scooter_button(self):
        # Ожидаем, пока элемент не станет кликабельным
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(LOGO_SCOOTER_BUTTON)
        )
        self.driver.find_element(*LOGO_SCOOTER_BUTTON).click()

    @allure.step("Проверка что после клика по кнопке 'Самокат' перешли на главную страницу")
    def check_url_home_scooter(self, expected_url):
        # Ожидаем загрузки страницы и получаем текущий URL
        current_url = self.driver.current_url
        # Сравниваем текущий URL с ожидаемым
        assert current_url == expected_url, f"Ожидаемый URL {expected_url}, но текущий {current_url}"
        # Логируем успех
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
        print(f"Текущий URL: {current_url}, Ожидаемый URL: {expected_url}")

    @allure.step("Кликаем на кнопку 'Яндекс' в логотипе")
    def click_yandex_logo_button(self):
        # Ожидаем, пока элемент не станет кликабельным
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((LOGO_YANDEX_BUTTON))
        )
        self.driver.find_element(*LOGO_YANDEX_BUTTON).click()

        # Ожидаем появления новой вкладки
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))  # Проверяем, что открылась новая вкладка
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)  # Переключаемся на новую вкладку

    @allure.step("Проверка, что открылась страница Яндекс Дзена")
    def check_url_dzen(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Ожидаемый URL: {expected_url}, но текущий: {current_url}"


    @allure.step("Ожидание загрузки главной страницы")
    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(LOGO_HOME_LOC))

