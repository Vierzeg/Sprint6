# about_rent_locators.py

from selenium.webdriver.common.by import By

# Локаторы полей
ORDER_HEADER_LOCATOR = (By.XPATH, "//div[text()='Про аренду']") #Заголовок Про аренду
DATE_FIELD_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/input') # Поле даты
RENTAL_PERIOD_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]') #Поле выбора срока аренды
BLACK_PEARL_CHECKBOX_LOCATOR = (By.XPATH, '//*[@id="black"]')#чек-бокс серного цвета
GREY_CHECKBOX_LOCATOR = (By.XPATH, '//*[@id="grey"]')#чек-бокс серого цвета
COMMENT_FIELD_LOCATOR = (By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and @placeholder='Комментарий для курьера']")#Поле комментрия
# Локтор кнопок
ORDER_BUTTON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button[2]')#Кнопка Заказть


DATE_ELEVEN_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[5]') #Дата 11.04.2025
DATE_FOURTEEN_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[1]') #Дата 14.04.2025
OPTION_THREE_LOCATOR = (By.XPATH, "//div[@aria-selected='false' and text()='трое суток']")#Выбор кол-ва дней аренды
OPTION_FIVE_LOCATOR = (By.XPATH, "//div[@aria-selected='false' and text()='пятеро суток']")#Выбор кол-ва дней аренды

CONFIRM_HEADER_LOCATOR = (By.XPATH, "//div[contains(text(), 'Хотите оформить заказ?')]")#Заголовок Хотите оформить заказ?
CONFIRM_YES_BUTTON_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[2]/button[2]')#Кнопка Да (By.XPATH, "//button[text()='Да']")

ORDER_HEADER_MODAL_LOCATOR = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[1]')

WINDOW_CONF_ORDER = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]')
