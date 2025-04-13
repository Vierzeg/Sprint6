# about_rent_locators.py

from selenium.webdriver.common.by import By

# Локаторы полей
ORDER_HEADER_LOCATOR = (By.CSS_SELECTOR, ".Order_Header__BZXOb") #Заголовок Про аренду
DATE_FIELD_LOCATOR = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")# Поле даты
RENTAL_PERIOD_LOCATOR = (By.XPATH, "//div[text()='* Срок аренды']")#Поле выбора срока аренды
BLACK_PEARL_CHECKBOX_LOCATOR = (By.XPATH, '//*[@id="black"]')#чек-бокс серного цвета
GREY_CHECKBOX_LOCATOR = (By.XPATH, '//*[@id="grey"]')#чек-бокс серого цвета
COMMENT_FIELD_LOCATOR = (By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and @placeholder='Комментарий для курьера']")#Поле комментрия
# Локтор кнопок
ORDER_BUTTON_LOCATOR = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")#Кнопка Заказть


DATE_ELEVEN_LOCATOR = (By.CSS_SELECTOR, ".react-datepicker__day--011")#Дата 11.04.2025
DATE_FOURTEEN_LOCATOR = (By.CSS_SELECTOR, ".react-datepicker__day--014") #Дата 14.04.2025
OPTION_THREE_LOCATOR = (By.XPATH, "//div[@aria-selected='false' and text()='трое суток']")#Выбор кол-ва дней аренды
OPTION_FIVE_LOCATOR = (By.XPATH, "//div[@aria-selected='false' and text()='пятеро суток']")#Выбор кол-ва дней аренды

CONFIRM_HEADER_LOCATOR = (By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ")
CONFIRM_YES_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Да']")
ORDER_HEADER_MODAL_LOCATOR = (By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ")

WINDOW_CONF_ORDER = (By.CSS_SELECTOR, ".Order_Modal__YZ-d3")