import time

from forms.admin_form import AdminForm
from forms.cart_form import CartForm
from forms.new_product_form import NewProductForm
from forms.new_user_form import NewUserForm
from forms.product_form import ProductForm
from forms.store_form import StoreForm


class FormFactory:
    def __init__(self, app):
        self.app = app
        self.admin_form = AdminForm(app)
        self.new_user_form = NewUserForm(app)
        self.new_product_form = NewProductForm(app)
        self.product_form = ProductForm(app)
        self.store_form = StoreForm(app)
        self.cart_form = CartForm(app)

    def open_admin_form(self):
        self.app.wd.get("http://localhost/litecart/admin")
        time.sleep(0.5)
        return self.admin_form

    def open_store_form(self):
        self.app.wd.get("http://localhost/litecart/en/")
        time.sleep(0.5)
        return self.store_form

    def open_new_user_form(self):
        self.app.wd.get("http://localhost/litecart/en/create_account")
        time.sleep(0.5)
        return self.new_user_form

    def open_new_product_form(self):
        self.admin_form.click_add_new_product()
        return self.new_product_form

    def open_first_product_card(self):
        self.store_form.open_first_product_card()
        return self.product_form

    def open_cart(self):
        self.store_form.open_cart()
        return self.cart_form
