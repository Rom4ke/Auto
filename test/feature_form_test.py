import allure
import pytest
from base.base_test import BaseTest

@allure.feature("forms")
class TestFormFeature(BaseTest):

    @allure.title("enter name and lastname")
    @allure.severity("critical")
    @pytest.mark.smoke
    def test_change_profile(self):
        self.form_page.open()
        self.form_page.enter_name(self.data.NAME)
        self.form_page.enter_lastname(self.data.LASTNAME)