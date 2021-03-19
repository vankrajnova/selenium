import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
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

    def add_products_to_cart(self):
        quantity = self._elements.quantity().text
        self._elements.products()[0].click()
        self._elements.add_to_cart_btn().click()
        count = int(quantity) + 1
        self.app.wait.until(EC.text_to_be_present_in_element((By.XPATH, """//span[contains(@class, "quantity")]"""), str(count)))

    def open_cart(self):
        self._elements.checkout().click()

    def remove_product(self):
        btn_1 = self._elements.remove_btn()[0]
        btn_2 = self._elements.remove_btn()[1]
        btn_3 = self._elements.remove_btn()[2]
        items = len(self._elements.remove_btn())
        for _ in range(5):
            btn_1.click()
            if items == int(items) - 1:
                return
            time.sleep(2)
        for _ in range(5):
            btn_2.click()
            if items == int(items) - 1:
                return
            time.sleep(2)
        for _ in range(5):
            btn_3.click()
            if items == int(items) - 1:
                return
            time.sleep(2)

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

    def verify_campaign_price_color_is_bold(self):
        campaign_price = self._elements.campaign_price()
        campaign_price_weight = campaign_price.value_of_css_property("font-weight")
        assert "700" == campaign_price_weight

    def verify_size_of_prices(self):
        campaign_price = self._elements.campaign_price()
        campaign_price_size = campaign_price.value_of_css_property("font-size").replace("px", "")
        regular_price = self._elements.regular_price()
        regular_price_size = regular_price.value_of_css_property("font-size").replace("px", "")
        assert int(campaign_price_size) > float(regular_price_size)

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

    def verify_campaign_price_color_is_bold_in_card(self):
        campaign_price_in_card = self._elements.campaign_price_in_card()
        campaign_price_in_card_weight = campaign_price_in_card.value_of_css_property("font-weight")
        assert "700" == campaign_price_in_card_weight

    def verify_size_of_prices_in_card(self):
        campaign_price_in_card = self._elements.campaign_price_in_card()
        campaign_price_in_card_size = campaign_price_in_card.value_of_css_property("font-size").replace("px", "")
        regular_price_in_card = self._elements.regular_price_in_card()
        regular_price_in_card_size = regular_price_in_card.value_of_css_property("font-size").replace("px", "")
        assert int(campaign_price_in_card_size) > int(regular_price_in_card_size)


class Elements:
    def __init__(self, app):
        self.app = app

    def items(self):
        xpath = """//td[contains(@class, 'item')]"""
        return self.app.wd.find_elements_by_xpath(xpath)

    def remove_btn(self):
        xpath = """//button[contains(@value, 'Remove')]"""
        return self.app.wd.find_elements_by_xpath(xpath)

    def checkout(self):
        xpath = """//a[contains(@class, 'link') and contains(text(), 'Checkout')]"""
        return self.app.wd.find_element_by_xpath(xpath)

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