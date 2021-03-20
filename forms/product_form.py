from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductForm:
    def __init__(self, app):
        self.app = app
        self._elements = Elements(app)

    def add_product_to_cart(self):
        quantity = self._elements.quantity().text
        self._elements.add_to_cart_btn().click()
        count = int(quantity) + 1
        self.app.wait.until(EC.text_to_be_present_in_element((By.XPATH, """//span[contains(@class, "quantity")]"""), str(count)))


class Elements:
    def __init__(self, app):
        self.app = app

    def add_to_cart_btn(self):
        xpath = """//button[contains(@name, 'add_cart_product')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def quantity(self):
        xpath = """//span[contains(@class, "quantity")]"""
        return self.app.wd.find_element_by_xpath(xpath)