import time


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


class Elements:
    def __init__(self, app):
        self.app = app

    @property
    def email(self):
        xpath = """//*[contains(@name, "email")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def password(self):
        xpath = """//*[contains(@name, "password")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def products(self):
        xpath = """//*[contains(@class, "box")]//*[contains(@class, "link")]"""
        return self.app.wd.find_elements_by_xpath(xpath)

    def logout_btn(self):
        xpath = """//*[contains(text(), "Logout")]"""
        return self.app.wd.find_elements_by_xpath(xpath)

    @property
    def login_btn(self):
        xpath = """//*[contains(@value, 'Login')]"""
        return self.app.wd.find_element_by_xpath(xpath)