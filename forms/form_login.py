from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class FormLogin:

    def __init__(self, app):
        self.app = app
        self.elements = Elements(self.app)

    def open(self):
        self.app.wd.get("https://www.github.com/login")
        self.app.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='login_field']")))

    def fill_login_field(self, text):
        self.app.enter_text(self.elements.login_field(), text)

    def fill_password_field(self, text):
        self.app.enter_text(self.elements.password_field(), text)

    def fill_login_form(self, login, password):
        self.fill_login_field(login)
        self.fill_password_field(password)

    def click_sign_in_btn(self):
        self.elements.sign_in_btn().click()

    def sign_in(self, login, password):
        self.open()
        self.fill_login_form(login, password)
        self.click_sign_in_btn()

    def get_alert_text(self):
        return self.elements.incorrect_login_pass_alert().text

class Elements:
    def __init__(self, app):
        self.app = app

    def login_field(self):
        xpath = "//*[@id='login_field']"
        return self.app.find_element_by_xpath(xpath)

    def password_field(self):
        xpath = "//*[@id='password']"
        return self.app.find_element_by_xpath(xpath)

    def sign_in_btn(self):
        xpath = "//input[@type='submit']"
        return self.app.find_element_by_xpath(xpath)

    def incorrect_login_pass_alert(self):
        xpath = "//div[@role='alert']"
        return self.app.find_element_by_xpath(xpath)

