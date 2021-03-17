from selenium import webdriver

from forms.factory import FormFactory


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        # self.wd = webdriver.Firefox()
        # self.wd = webdriver.Ie()
        self.wd.implicitly_wait(5)
        self.forms = FormFactory(self)

    def destroy(self):
        self.wd.quit()
