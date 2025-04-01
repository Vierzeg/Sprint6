# test_text_imp_qst_page.py


class TestListQuestion:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(url)
        cls.qst_of_list = PageImportantQuestion(cls.driver)
    def test_text_list_question1(self):
        self.click_list_button()
        self.check_list_text()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

