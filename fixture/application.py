from selenium import webdriver
from form_factory import FormFactory
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep


class Application:
    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        self.forms = FormFactory(self)
        self._wait_sec_default = 10
        self.wait = WebDriverWait(self.wd, self._wait_sec_default)

    def destroy(self):
        self.wd.quit()

    def find_element_by_xpath(self, xpath):
        return self.wd.find_element(By.XPATH, xpath)

    def find_elements_by_xpath(self, xpath):
        return self.wd.find_elements(By.XPATH, xpath)

    def enter_text(self, element, text):
        element.click()
        element.clear()
        for letter in text:
            element.send_keys(letter)
            sleep(0.05)


