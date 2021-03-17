import time
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait


class StoreForm:
    def __init__(self, app):
        self.app = app
        self._elements = Elements(app)

    def verify_products_has_one_sticker(self):
        products = self._elements.products()
        for product in products:
            stickers = product.find_elements_by_xpath(""".//*[contains(@class, "sticker")]""")
            assert len(stickers) == 1

    def login(self, email, password):
        self._elements.email.send_keys(email)
        self._elements.password.send_keys(password)
        self._elements.login_btn.click()
        time.sleep(3)

    def logout(self):
        self._elements.logout_btn()[0].click()
        time.sleep(1)

    def open_duck_card(self):
        self._elements.duck().click()

    def verify_product(self):
        duck_name = self._elements.duck_name().text
        regular_price = self._elements.regular_price().text
        campaign_price = self._elements.campaign_price().text

        self.open_duck_card()

        duck_name_in_card = self._elements.duck_name_in_card().text
        regular_price_in_card = self._elements.regular_price_in_card().text
        campaign_price_in_card = self._elements.campaign_price_in_card().text

        assert duck_name == duck_name_in_card
        assert regular_price == regular_price_in_card
        assert campaign_price == campaign_price_in_card

    def verify_regular_price_color_is_gray(self):
        regular_price = self._elements.regular_price()
        regular_price_color = regular_price.value_of_css_property("color")
        s = regular_price_color.replace("rgba(", "").replace(")", "")
        l = s.split(", ")
        r = l[0]
        g = l[1]
        b = l[2]
        assert r == g == b

    def verify_regular_price_is_through(self):
        regular_price = self._elements.regular_price()
        text_decoration = regular_price.value_of_css_property("text-decoration-line")
        assert "line-through" == text_decoration

    def verify_campaign_price_color_is_red(self):
        campaign_price = self._elements.campaign_price()
        campaign_price_color = campaign_price.value_of_css_property("color")
        s = campaign_price_color.replace("rgba(", "").replace(")", "")
        l = s.split(", ")
        g = l[1]
        b = l[2]
        assert int(g) == 0
        assert int(b) == 0

    def verify_size_of_prices(self):
        campaign_price = self._elements.campaign_price()
        campaign_price_size = campaign_price.size
        regular_price = self._elements.regular_price()
        regular_price_size = regular_price.size
        assert campaign_price_size.get('height') > regular_price_size.get('height')
        assert campaign_price_size.get('width') > regular_price_size.get('width')

    def verify_regular_price_color_is_gray_in_card(self):
        regular_price_in_card = self._elements.regular_price_in_card()
        regular_price_in_card_color = regular_price_in_card.value_of_css_property("color")
        s = regular_price_in_card_color.replace("rgba(", "").replace(")", "")
        l = s.split(", ")
        r = l[0]
        g = l[1]
        b = l[2]
        assert r == g == b

    def verify_regular_price_is_through_in_card(self):
        regular_price_in_card = self._elements.regular_price_in_card()
        text_decoration = regular_price_in_card.value_of_css_property("text-decoration-line")
        assert "line-through" == text_decoration

    def verify_campaign_price_color_is_red_in_card(self):
        campaign_price_in_card = self._elements.campaign_price_in_card()
        campaign_price_in_card_color = campaign_price_in_card.value_of_css_property("color")
        s = campaign_price_in_card_color.replace("rgba(", "").replace(")", "")
        l = s.split(", ")
        g = l[1]
        b = l[2]
        assert int(g) == 0
        assert int(b) == 0

    def verify_size_of_prices_in_card(self):
        campaign_price_in_card = self._elements.campaign_price_in_card()
        campaign_price_in_card_size = campaign_price_in_card.size
        regular_price_in_card = self._elements.regular_price_in_card()
        regular_price_in_card_size = regular_price_in_card.size
        assert campaign_price_in_card_size.get('height') > regular_price_in_card_size.get('height')
        assert campaign_price_in_card_size.get('width') > regular_price_in_card_size.get('width')


class Elements:
    def __init__(self, app):
        self.app = app

    def duck(self):
        xpath = """//*[contains(@id, 'box-campaigns')]//li"""
        return self.app.wd.find_element_by_xpath(xpath)

    def duck_name_in_card(self):
        xpath = """//h1[contains(@class, 'title')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def regular_price_in_card(self):
        xpath = """//*[contains(@class, 'regular-price')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def campaign_price_in_card(self):
        xpath = """//*[contains(@class, 'campaign-price')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def duck_name(self):
        xpath = """//*[contains(@id, 'box-campaigns')]//*[contains(@class, 'name')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def regular_price(self):
        xpath = """//*[contains(@id, 'box-campaigns')]//*[contains(@class, 'regular-price')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def campaign_price(self):
        xpath = """//*[contains(@id, 'box-campaigns')]//*[contains(@class, 'campaign-price')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def add_to_cart_btn(self):
        xpath = """//button[contains(@name, 'add_cart_product')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def quantity(self):
        xpath = """//span[contains(@class, "quantity")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def email(self):
        xpath = """//*[contains(@name, "email")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def password(self):
        xpath = """//*[contains(@name, "password")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def products(self):
        xpath = """//li[contains(@class, "product")]"""
        return self.app.wd.find_elements_by_xpath(xpath)

    def logout_btn(self):
        xpath = """//*[contains(text(), "Logout")]"""
        return self.app.wd.find_elements_by_xpath(xpath)

    @property
    def login_btn(self):
        xpath = """//*[contains(@value, 'Login')]"""
        return self.app.wd.find_element_by_xpath(xpath)