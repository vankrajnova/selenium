from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from forms.factory import FormFactory


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        # self.wd = webdriver.Firefox()
        # self.wd = webdriver.Ie()
        self.wait = WebDriverWait(self.wd, 10)
        self.wd.implicitly_wait(10)
        self.forms = FormFactory(self)

    def destroy(self):
        self.wd.quit()
