# conftest.py

import pytest
from selenium import webdriver
from helpers.url_holders import url_home
from pages.imp_qst_page import PageImportantQuestion

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.get(url_home)
    qst_of_list = PageImportantQuestion(driver)
    qst_of_list.close_cookie_banner()
    yield qst_of_list
    driver.quit()