import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(scope = "class")
def setup(request):
    """
    Set-ups the environment for the tests.
    """
    chrome_options: ChromeOptions = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--ignore-certificate-errors")
    service_obj = Service("/home/student/tester/chromedriver-linux64/chromedriver")
    driver = webdriver.Chrome(service=service_obj, options= chrome_options)
    # driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()