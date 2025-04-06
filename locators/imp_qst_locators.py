# imp_qst_locators.py

from selenium.webdriver.common.by import By

# Локаторы выпадающих списков с вопросами
QUESTION_LOCATORS = [
    (By.XPATH, "//div[@class='accordion__button' and text()='Сколько это стоит? И как оплатить?']"),
    (By.ID, "accordion__heading-1"),
    (By.ID, "accordion__heading-2"),
    (By.ID, "accordion__heading-3"),
    (By.ID, "accordion__heading-4"),
    (By.ID, "accordion__heading-5"),
    (By.ID, "accordion__heading-6"),
    (By.ID, "accordion__heading-7")
]

# Локаторы содержимого элементов выпадающего списка
TEXT_LOCATORS = [
    (By.ID, "accordion__panel-0"),
    (By.ID, "accordion__panel-1"),
    (By.ID, "accordion__panel-2"),
    (By.ID, "accordion__panel-3"),
    (By.ID, "accordion__panel-4"),
    (By.ID, "accordion__panel-5"),
    (By.ID, "accordion__panel-6"),
    (By.ID, "accordion__panel-7")
]

