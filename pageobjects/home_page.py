from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class HomePage:

    MY_ACCOUNT: tuple = (By.CSS_SELECTOR, "li[id='menu-item-22'] a[class='nav__link']")

    def __init__(self, driver):
        self._driver = driver

    def get_my_account_link(self):
        return self._driver.find_element(*HomePage.MY_ACCOUNT)


