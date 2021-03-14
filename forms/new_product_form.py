import os
import random
import time

from selenium.webdriver.common.by import By


class NewProductForm:
    def __init__(self, app):
        self.app = app
        self._elements = Elements(app)

    def fill_form(self, product_name):
        self.fill_general_tab(product_name)
        self.fill_information_tab()
        self.fill_prices_tab()
        self._elements.save_btn().click()
        time.sleep(1)

    def fill_general_tab(self, product_name):
        self._elements.enabled_btn().click()
        self._elements.name().send_keys(product_name)
        self._elements.code().send_keys("2802")
        self._elements.subcategory_checkbox().click()
        self._elements.quantity().clear()
        self._elements.quantity().send_keys("5")
        self._elements.image().send_keys(os.getcwd() + "/pug.jpg")
        self._elements.date_valid_from().send_keys("12.03.2021")
        self._elements.date_valid_to().send_keys("12.03.2022")

    def fill_information_tab(self):
        self._elements.tab_information_btn().click()
        time.sleep(1)
        self._elements.keywords().send_keys("2802")
        self._elements.short_description().send_keys("Test")
        self._elements.description().send_keys("Test")
        self._elements.head_title().send_keys("Pug")
        self._elements.meta_description().send_keys("Test")
        time.sleep(0.5)

    def fill_prices_tab(self):
        self._elements.tab_prices_btn().click()
        time.sleep(1)
        self._elements.purchase_price().clear()
        self._elements.purchase_price().send_keys("5")
        self._elements.select_usd_in_price()
        self._elements.prices_usd().clear()
        self._elements.prices_usd().send_keys("5")
        self._elements.prices_eur().clear()
        self._elements.prices_eur().send_keys("7")


class Elements:
    def __init__(self, app):
        self.app = app

    def enabled_btn(self):
        xpath = """//label[contains(text(), "Enabled")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def name(self):
        xpath = """//input[contains(@name, "name[en]")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def code(self):
        xpath = """//input[contains(@name, "code")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def subcategory_checkbox(self):
        xpath = """//input[contains(@value, '1-2')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def quantity(self):
        xpath = """//input[contains(@name, 'quantity')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def image(self):
        xpath = """//input[contains(@type, 'file')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def date_valid_from(self):
        xpath = """//input[contains(@name, 'date_valid_from')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def date_valid_to(self):
        xpath = """//input[contains(@name, 'date_valid_to')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def tab_information_btn(self):
        xpath = """//a[contains(text(), 'Information')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def tab_prices_btn(self):
        xpath = """//a[contains(text(), 'Prices')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def keywords(self):
        xpath = """//input[contains(@name, 'keywords')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def short_description(self):
        xpath = """//input[contains(@name, 'short_description[en]')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def description(self):
        xpath = """//*[contains(@dir, "ltr")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def head_title(self):
        xpath = """//input[contains(@name, 'head_title[en]')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def meta_description(self):
        xpath = """//input[contains(@name, 'meta_description[en]')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def purchase_price(self):
        xpath = """//input[contains(@name, "purchase_price")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def select_usd_in_price(self):
        select = self.app.wd.find_element_by_xpath("""//select[contains(@name, "purchase_price_currency_code")]""")
        self.app.wd.execute_script("arguments[0].selectedIndex=1; arguments[0].dispatchEvent(new Event('change'))",
                                   select)

    def prices_usd(self):
        xpath = """//input[contains(@name, "prices[USD]")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def prices_eur(self):
        xpath = """//input[contains(@name, "prices[EUR]")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def save_btn(self):
        xpath = """//button[contains(@name, "save")]"""
        return self.app.wd.find_element_by_xpath(xpath)
