import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def open_login_page(driver):
    driver.get("http://localhost/litecart/admin")
    time.sleep(0.5)


def login_as_admin(driver):
    driver.find_element_by_xpath("""//input[contains(@name, 'username')]""").send_keys("admin")
    driver.find_element_by_xpath("""//input[contains(@name, 'password')]""").send_keys("admin")
    driver.find_element_by_xpath("""//*[contains(@value, 'Login')]""").click()
    time.sleep(0.5)


def click_menu_buttons(driver):
    top_level_xpath = """//*[contains(@id, 'app-')]"""
    sub_level_xpath = """//*[contains(@id, "doc-")]"""

    elements = driver.find_elements_by_xpath(top_level_xpath)
    if len(elements) > 0:
        for i in range(len(driver.find_elements_by_xpath(top_level_xpath))):
            driver.find_elements_by_xpath(top_level_xpath)[i].click()
            time.sleep(1)
            assert is_element_present(driver)
            for i in range(len(driver.find_elements_by_xpath(sub_level_xpath))):
                driver.find_elements_by_xpath(sub_level_xpath)[i].click()
                time.sleep(1)
                assert is_element_present(driver)


def is_element_present(driver):
    elements = driver.find_elements(By.TAG_NAME, "h1")
    return len(elements) > 0


def test_login(driver):
    open_login_page(driver)

    login_as_admin(driver)


def test_task_7(driver):
    open_login_page(driver)

    login_as_admin(driver)

    click_menu_buttons(driver)
