import random
import time


class NewUserForm:
    def __init__(self, app):
        self.app = app
        self._elements = Elements(app)

    def create_user(self, email, password):
        self.fill_form(email, password)
        self.click_create_btn()

    def fill_form(self, email, password):
        self._elements.first_name.send_keys("Test")
        self._elements.last_name.send_keys("Test")
        self._elements.address_1.send_keys("Test")
        self._elements.postcode.send_keys("123123")
        self._elements.city.send_keys("Moscow")
        self._elements.email.send_keys(email)
        self._elements.phone.send_keys("+79656321445")
        self._elements.desired_password.send_keys(password)
        self._elements.confirm_password.send_keys(password)

    def click_create_btn(self):
        self._elements.create_account_btn.click()
        time.sleep(1)


class Elements:
    def __init__(self, app):
        self.app = app

    @property
    def first_name(self):
        xpath = """//*[contains(@name, 'firstname')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def last_name(self):
        xpath = """//*[contains(@name, 'lastname')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def address_1(self):
        xpath = """//*[contains(@name, 'address1')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def postcode(self):
        xpath = """//*[contains(@name, 'postcode')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def city(self):
        xpath = """//*[contains(@name, 'city')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def email(self):
        xpath = """//*[contains(@name, 'email')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def phone(self):
        xpath = """//*[contains(@name, 'phone')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def desired_password(self):
        xpath = """//*[contains(@name, 'password')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def confirm_password(self):
        xpath = """//*[contains(@name, 'confirmed_password')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def create_account_btn(self):
        xpath = """//*[contains(@name, 'create_account')]"""
        return self.app.wd.find_element_by_xpath(xpath)
