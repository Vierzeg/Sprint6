# base_page_locators.py

from selenium.webdriver.common.by import By

COOKIE_BANNER_LOC = (By.XPATH, "//div[@class='App_CookieText__1sbqp' and text()='И здесь куки! В общем, мы их используем.']")
COOKIE_BUTTON_LOC = (By.XPATH, "//button[text()='да все привыкли']")
LOGO_HOME_LOC = (By.CLASS_NAME, "Header_Disclaimer__3VEni")
