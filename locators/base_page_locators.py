# base_page_locators.py

from selenium.webdriver.common.by import By

COOKIE_BANNER_LOC = (By.XPATH, "//div[@class='App_CookieText__1sbqp' and text()='И здесь куки! В общем, мы их используем.']")
COOKIE_BUTTON_LOC = (By.XPATH, "//button[text()='да все привыкли']")
LOGO_HOME_LOC = (By.CLASS_NAME, "Header_Disclaimer__3VEni")

# Локаторы кнопок
ORDER_BUTTON_SMALL = (By.CLASS_NAME, "Button_Button__ra12g")
ORDER_BUTTON_BIG = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_UltraBig__UU3Lp")
LOGO_YANDEX_BUTTON = (By.XPATH, "//a[@href='//yandex.ru']")
LOGO_SCOOTER_BUTTON = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']//img[@alt='Scooter']")

