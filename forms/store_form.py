class StoreForm:
    def __init__(self, app):
        self.app = app
        self._elements = Elements(app)

    def verify_products_has_one_sticker(self):
        products = self._elements.products()
        for product in products:
            stickers = product.find_elements_by_xpath(""".//*[contains(@class, "sticker")]""")
            assert len(stickers) == 1


class Elements:
    def __init__(self, app):
        self.app = app

    def products(self):
        xpath = """//*[contains(@class, "product column shadow hover-light")]"""
        return self.app.wd.find_elements_by_xpath(xpath)
