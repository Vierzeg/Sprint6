# base_page_locators.py

from selenium.webdriver.common.by import By

COOKIE_BANNER_LOC = (By.XPATH, "//div[@class='App_CookieText__1sbqp' and text()='И здесь куки! В общем, мы их используем.']")
COOKIE_BUTTON_LOC = (By.XPATH, "//button[text()='да все привыкли']")
LOGO_HOME_LOC = (By.CLASS_NAME, "Header_Disclaimer__3VEni")

# Локаторы кнопок
#ORDER_BUTTON_SMALL = (By.XPATH, "/html/body/div/div/div/div[1]/div[2]/button[1]")
#ORDER_BUTTON_SMALL = (By.CSS_SELECTOR, "button.Button_Button__ra12g:contains('Заказать')")
ORDER_BUTTON_SMALL = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[2]/button[1]")
ORDER_BUTTON_BIG = (By.XPATH, "//*[@id='root']//button")
LOGO_YANDEX_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/a[1]')
LOGO_SCOOTER_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/a[2]/img')

