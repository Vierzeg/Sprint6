# imp_qst_page.py

from locators.imp_qst_locators import *
class PageImportantQuestion:
# Описание элементов
    question_1 = [*QUESTION_LOC1]
    question_2 = [*QUESTION_LOC2]
    question_3 = [*QUESTION_LOC3]
    question_4 = [*QUESTION_LOC4]
    question_5 = [*QUESTION_LOC5]
    question_6 = [*QUESTION_LOC6]
    question_7 = [*QUESTION_LOC7]
    question_8 = [*QUESTION_LOC8]

    qst_text_1 = [*text_qst1]
    qst_text_2 = [*text_qst2]
    qst_text_3 = [*text_qst3]
    qst_text_4 = [*text_qst4]
    qst_text_5 = [*text_qst5]
    qst_text_6 = [*text_qst6]
    qst_text_7 = [*text_qst7]
    qst_text_8 = [*text_qst8]
# Создаем драйвер
    def __init__(self,driver):
        self.driver = driver

    def click_list_button(self):
        self.driver.find_element(question_1)

    def check_list_text(self):
        actually_set_text = self.driver.find_element()
        expected_set_text = qst_text
        assert  actually_set_text == expected_set_text

    def wait_for_load_home_page(self):

    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.HOME_LOGO_LOC))