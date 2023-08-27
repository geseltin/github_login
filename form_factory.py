from forms.form_login import FormLogin
from forms.form_main import MainPage


class FormFactory:
    def __init__(self, app):
        self.form_login = FormLogin(app)
        self.form_main = MainPage(app)