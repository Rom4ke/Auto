import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class FormPage(BasePage):

    PAGE_URL = Links.FORMS

    USERNAME_FIELD = ("xpath", "//input[@id='firstName']")
    LASTNAME_FIELD = ("xpath", "//input[@id='lastName']")

    @allure.step("Enter name")
    def enter_name(self, name):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(name)

    @allure.step("Enter lastname")
    def enter_lastname(self, last_name):
        self.wait.until(EC.element_to_be_clickable(self.LASTNAME_FIELD)).send_keys(last_name)
