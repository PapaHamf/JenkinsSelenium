from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class LoginPage:

    REG_MAIL_ADDR: tuple = (By.ID, "reg_email")
    REG_PASSWD: tuple = (By.ID, "reg_password")
    REG_BUTTON: tuple = (By.CSS_SELECTOR, "button[value='Register']")

    LOG_MAIL_ADDR: tuple = (By.ID, "username")
    LOG_PASSWD: tuple = (By.ID, "password")
    LOG_BUTTON: tuple = (By.CSS_SELECTOR, "button[value='Log in']")

    def __init__(self, driver):
        self._driver = driver

    def get_email_add(self):
        return self._driver.find_element(*LoginPage.REG_MAIL_ADDR)

    def get_passwd_reg(self):
        return self._driver.find_element(*LoginPage.REG_PASSWD)

    def get_reg_button(self):
        return self._driver.find_element(*LoginPage.REG_BUTTON)

    def get_log_email_add(self):
        return self._driver.find_element(*LoginPage.LOG_MAIL_ADDR)

    def get_log_passwd(self):
        return self._driver.find_element(*LoginPage.LOG_PASSWD)

    def get_log_button(self):
        return self._driver.find_element(*LoginPage.LOG_BUTTON)