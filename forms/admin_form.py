import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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

    def open_countries_tab(self):
        self._elements.menu_btn_countries().click()
        time.sleep(1)

    def open_geo_zones_tab(self):
        self.app.wd.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')

    def open_catalog_tab(self):
        self.app.wd.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')

    def open_new_country_form(self):
        self._elements.add_new_country_btn().click()

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

    def open_all_external_links(self):
        for i in range(len(self._elements.external_links())):
            current_window = self.app.wd.current_window_handle
            old_windows = self.app.wd.window_handles
            self._elements.external_links()[i].click()
            self.app.wait.until(EC.new_window_is_opened(old_windows))
            new_window = [i for i in self.app.wd.window_handles if i not in old_windows]
            self.app.wd.switch_to.window(new_window[0])
            self.app.wd.close()
            self.app.wd.switch_to.window(current_window)

    def verify_product_presents(self, product_name):
        assert self._elements.is_product_present(product_name) == 1

    def verify_sort_zones_in_geo_zone(self):
        href_list = self._elements.get_href_list_for_geo_zones()
        for href in href_list:
            self.app.wd.get(href)
            time.sleep(0.5)
            actual_list = self._elements.get_zone_name_list_in_geo_zone()
            expected_list = self._elements.get_zone_name_list_in_geo_zone()
            expected_list.sort()
            assert expected_list == actual_list

    def verify_sort_for_all_country(self):
        actual_list = self._elements.get_country_name_list()
        expected_list = self._elements.get_country_name_list()
        expected_list.sort()
        assert expected_list == actual_list

    def verify_sort_zones_in_country(self):
        href_list = self._elements.get_href_list_for_country_with_zones()
        for href in href_list:
            self.app.wd.get(href)
            time.sleep(0.5)
            actual_list = self._elements.get_zone_name_list()
            expected_list = self._elements.get_zone_name_list()
            expected_list.sort()
            assert expected_list == actual_list

    def verify_log_is_empty(self):
        href_list = self._elements.get_href_list_for_products()
        for href in href_list:
            self.app.wd.get(href)
            log = self.app.wd.get_log("browser")
            if len(log) != 0:
                print(log)


class Elements:
    def __init__(self, app):
        self.app = app

    def get_href_list_for_products(self):
        all_row = self.app.wd.find_elements_by_xpath("""//a[contains(@title, "Edit")]""")
        href_list = []
        for row in all_row:
            href_list.append(row.get_attribute("href"))
        return href_list

    def get_href_list_for_geo_zones(self):
        all_row = self.app.wd.find_elements_by_xpath("""//a[contains(@title, "Edit")]""")
        href_list = []
        for row in all_row:
            href_list.append(row.get_attribute("href"))
        return href_list

    def get_href_list_for_country_with_zones(self):
        all_row = self.app.wd.find_elements_by_xpath("""//tr[contains(@class, "row")]""")
        href_list = []
        for row in all_row:
            link = row.find_element_by_xpath(".//td//a")
            zone = row.find_elements_by_xpath(".//td")[5].text
            if zone != "0":
                href_list.append(link.get_attribute("href"))
        return href_list

    def get_country_name_list(self):
        all_row = self.app.wd.find_elements_by_xpath("""//tr[contains(@class, "row")]""")
        country_name_list = []
        for row in all_row:
            cells = row.find_elements_by_xpath(".//td")
            name = cells[4].text
            country_name_list.append(name)
        return country_name_list

    def get_zone_name_list_in_geo_zone(self):
        zone_name_list = []
        all_zones_name = self.app.wd.find_elements_by_xpath("""//select[contains(@name, '[zone_code]')]//option[
        contains(@selected, 'selected')]""")
        for name in all_zones_name:
            text = name.get_attribute("innerText")
            zone_name_list.append(text)
        return zone_name_list

    def get_zone_name_list(self):
        zone_name_list = []
        all_zones_name = self.app.wd.find_elements_by_xpath("""//*[contains(@name, '][name]')]""")
        for name in all_zones_name:
            text = name.get_attribute("value")
            zone_name_list.append(text)
        return zone_name_list

    def is_product_present(self, product_name):
        xpath = """//a[contains(text(), '{}')]"""
        element = self.app.wd.find_elements_by_xpath(xpath.format(product_name))
        return len(element) > 0

    def is_header_present(self):
        elements = self.app.wd.find_elements(By.TAG_NAME, "h1")
        return len(elements) > 0

    def external_links(self):
        xpath = """//i[contains(@class, 'fa-external-link')]"""
        return self.app.wd.find_elements_by_xpath(xpath)

    def add_new_country_btn(self):
        xpath = """//a[contains(text(), ' Add New Country')]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def top_level_buttons(self):
        xpath = """//*[contains(@id, 'app-')]"""
        return self.app.wd.find_elements_by_xpath(xpath)

    def sub_level_buttons(self):
        xpath = """//*[contains(@id, "doc-")]"""
        return self.app.wd.find_elements_by_xpath(xpath)

    def menu_btn_catalog(self):
        xpath = """//span[contains(text(), "Catalog")]"""
        return self.app.wd.find_element_by_xpath(xpath)

    def menu_btn_countries(self):
        xpath = """//span[contains(text(), "Countries")]"""
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
