# for_who_locators.py

from selenium.webdriver.common.by import By

# Локаторы полей
HEADLINE_FOR_WHO_LOCATOR = (By.XPATH, "//div[text()='Для кого самокат']")
NAME_FIELD_LOCATOR = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/input")
SEC_NAME_FIELD_LOCATOR = (By.XPATH, "//div[@id='root']//div[2]//div[2]//div[2]//input")
ADDRESS_FIELD_LOCATOR = (By.CSS_SELECTOR, "input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder='* Адрес: куда привезти заказ']")
METRO_FIELD_LOCATOR = (By.XPATH, "//div[@id='root']//div[2]//div[2]//div[4]//div//input")
CHOOSE_ELEM_LOCATOR = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[4]")

TEL_FIELD_LOCATOR = (By.XPATH, "//div[@id='root']//div[2]//div[2]//div[5]//input")

NEXT_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(),'Далее')]")
