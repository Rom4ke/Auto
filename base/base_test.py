import pytest
from config.data import Data
from pages.form_page import FormPage

class BaseTest:

    data: Data

    form_page: FormPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.form_page = FormPage(driver)