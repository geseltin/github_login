from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class MainPage:

    def __init__(self, app):
        self.app = app
        self.elements = Elements(self.app)

    def current_user_login(self):
        return self.elements.user_login()

    def is_logged_in(self):
        if len(self.app.find_elements_by_xpath("//*[contains(text(), 'Sign out')]")) > 0:
            return True
        else:
            return False

    def logout(self):
        self.app.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='Button-content']//img[@class='avatar circle']")))
        self.elements.side_menu().click()
        self.app.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@href='/logout']")))
        self.elements.logout_btn_main().click()
        self.app.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Sign out']")))
        self.elements.logout_btn_additional().click()


    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()


class Elements:
    def __init__(self, app):
        self.app = app

    def user_login(self):
        xpath = "//meta[@name='user-login']"
        return self.app.find_element_by_xpath(xpath).get_property('content')

    def logout_btn_main(self):
        xpath = "//*[@href='/logout']"
        return self.app.find_element_by_xpath(xpath)

    def side_menu(self):
        xpath = "//span[@class='Button-content']//img[@class='avatar circle']"
        return self.app.find_element_by_xpath(xpath)

    def logout_btn_additional(self):
        xpath = "//input[@value='Sign out']"
        return self.app.find_element_by_xpath(xpath)

