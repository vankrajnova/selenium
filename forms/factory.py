import time

from forms.admin_form import AdminForm
from forms.new_user_form import NewUserForm
from forms.store_form import StoreForm


class FormFactory:
    def __init__(self, app):
        self.app = app
        self.admin_form = AdminForm(app)
        self.new_user_form = NewUserForm(app)
        self.store_form = StoreForm(app)

    def open_admin_form(self):
        self.app.wd.get("http://localhost/litecart/admin")
        time.sleep(0.5)
        return self.admin_form

    def open_store_page(self):
        self.app.wd.get("http://localhost/litecart/en/")
        time.sleep(0.5)
        return self.store_form


