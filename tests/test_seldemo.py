import pytest
import time
import allure

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

    @allure.parent_suite("Tests for Selenium demo")
    @allure.suite("Tests for customer login")
    @allure.tag("Account login", "User login")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("Test case no 1")
    @allure.description("This test attempts to log in on the user account.")
    def test_user_login(self):
        self.driver.get(TestRegister.URL)
        login_page = LoginPage(self.driver)
        with allure.step("Step 1: Enter the username"):
            login_page.get_log_email_add().send_keys("mareczek@testowy.pl")
        with allure.step("Step 2: Enter the password"):
            login_page.get_log_passwd().send_keys("mareczek1234$")
        with allure.step("Step 3: Clicking the button"):
            login_page.get_log_button().click()
        time.sleep(5)