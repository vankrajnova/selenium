import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_xpath("""//input[contains(@name, 'username')]""").send_keys("admin")
    driver.find_element_by_xpath("""//input[contains(@name, 'password')]""").send_keys("admin")
    driver.find_element_by_xpath("""//*[contains(@name, 'login')]""").click()
