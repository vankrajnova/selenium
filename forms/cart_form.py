from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartForm:
    def __init__(self, app):
        self.app = app
        self._elements = Elements(app)

    def stop_action(self):
        """Останавливает движение картинок"""
        self.app.wait.until(EC.element_to_be_clickable((By.XPATH, """//li//a[contains(@class, 'inact')]""")))
        pictures = self._elements.pictures()
        for picture in pictures:
            picture.click()

    def remove_all_products(self):
        self.app.wait.until(EC.presence_of_element_located((By.XPATH, self._elements.confirm_btn_xpath)))
        self.stop_action()
        self._elements.pictures()[0].click()
        self.app.wait.until(EC.element_to_be_clickable((By.XPATH, self._elements.remove_btn_xpath)))
        items = self._elements.items()
        for _ in items:
            table = self._elements.table_with_products()
            self._elements.remove_buttons()[0].click()
            self.app.wait.until(EC.staleness_of(table))
            new_items = self._elements.items()
            if len(new_items) == 0:
                self.app.wait.until(
                    EC.text_to_be_present_in_element((By.XPATH, """//em"""), "There are no items in your cart."))


class Elements:
    def __init__(self, app):
        self.app = app

    def table_with_products(self):
        xpath = """//table[contains(@class, "dataTable")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    @property
    def confirm_btn_xpath(self):
        xpath = "//button[contains(@name, 'confirm_order')]"
        return xpath

    def pictures(self):
        xpath = """//li//a[contains(@class, 'inact')]"""
        return self.app.wd.find_elements_by_xpath(xpath)

    def items(self):
        xpath = """//td[contains(@class, 'item')]"""
        return self.app.wd.find_elements_by_xpath(xpath)

    @property
    def remove_btn_xpath(self):
        xpath = """//button[contains(@value, 'Remove')]"""
        return xpath

    def remove_buttons(self):
        xpath = """//button[contains(@value, 'Remove')]"""
        return self.app.wd.find_elements_by_xpath(xpath)
