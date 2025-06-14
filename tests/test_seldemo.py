import pytest
import time

from pageobjects.login_page import LoginPage
from utils.baseclass import BaseClass

class TestRegister(BaseClass):

    URL: str = "http://seleniumdemo.com/?page_id=7"

    @pytest.mark.skip
    def test_user_registration(self):
        self.driver.get(TestRegister.URL)
        login_page = LoginPage(self.driver)
        login_page.get_email_add().send_keys("mareczek@testowy.pl")
        login_page.get_passwd_reg().send_keys("mareczek1234$")
        login_page.get_reg_button().click()
        time.sleep(5)

    def test_user_login(self):
        self.driver.get(TestRegister.URL)
        login_page = LoginPage(self.driver)
        login_page.get_log_email_add().send_keys("mareczek@testowy.pl")
        login_page.get_log_passwd().send_keys("mareczek1234$")
        login_page.get_log_button().click()
        time.sleep(5)