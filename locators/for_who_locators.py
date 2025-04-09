# for_who_locators.py

from selenium.webdriver.common.by import By

# Локаторы полей
HEADLINE_FOR_WHO_LOCATOR = (By.CSS_SELECTOR, ".Order_Header__BZXOb")
NAME_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='* Имя']")
SEC_NAME_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='* Фамилия']")
ADDRESS_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
METRO_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='* Станция метро']")
CHOOSE_ELEM_LOCATOR = (By.CLASS_NAME, "select-search__select")
TEL_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

NEXT_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(),'Далее')]")
