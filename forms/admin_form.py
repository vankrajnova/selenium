import time

from selenium.webdriver.common.by import By

from forms.new_product_form import NewProductForm


class AdminForm:
    def __init__(self, app):
        self.app = app
        self._elements = Elements(app)

    def login_as_admin(self):
        self._elements.login.send_keys("admin")
        self._elements.password.send_keys("admin")
        self._elements.btn_login.click()
        time.sleep(0.5)

    def click_add_new_product(self):
        self._elements.menu_btn_catalog().click()
        self._elements.add_new_product_btn().click()
        time.sleep(1)

    def click_all_menu_buttons(self):
        elements = self._elements.top_level_buttons()
        if len(elements) > 0:
            for i in range(len(self._elements.top_level_buttons())):
                self._elements.top_level_buttons()[i].click()
                time.sleep(1)
                assert self._elements.is_header_present()
                for i in range(len(self._elements.sub_level_buttons())):
                    self._elements.sub_level_buttons()[i].click()
                    time.sleep(1)
                    assert self._elements.is_header_present()

    def verify_product_presents(self, product_name):
        assert self._elements.is_product_present(product_name) == 1


class Elements:
    def __init__(self, app):
        self.app = app

    def is_product_present(self, product_name):
        xpath = """//a[contains(text(), '{}')]"""
        element = self.app.wd.find_elements_by_xpath(xpath.format(product_name))
        return len(element) > 0

    def is_header_present(self):
        elements = self.app.wd.find_elements(By.TAG_NAME, "h1")
        return len(elements) > 0

    def top_level_buttons(self):
        xpath = """//*[contains(@id, 'app-')]"""
        return self.app.wd.find_elements_by_xpath(xpath)

    def sub_level_buttons(self):
        xpath = """//*[contains(@id, "doc-")]"""
        return self.app.wd.find_elements_by_xpath(xpath)

    def menu_btn_catalog(self):
        xpath = """//span[contains(text(), "Catalog")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def add_new_product_btn(self):
        xpath = """//a[contains(text(), " Add New Product")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def login(self):
        xpath = """//input[contains(@name, 'username')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def password(self):
        xpath = """//input[contains(@name, 'password')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def btn_login(self):
        xpath = """//*[contains(@value, 'Login')]"""
        return self.app.wd.find_element_by_xpath(xpath)
