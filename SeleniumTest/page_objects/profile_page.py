from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ProfilePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open_from_home(self):
        driver = self._driver
        driver.find_element(By.CLASS_NAME, "dropdown-toggle").click()
        driver.find_element(By.XPATH, "//a[contains(.,'Profile')]").click()

    def check_user_name(self, name, last_name):
        name_element = self._driver.find_element(By.CLASS_NAME, "profile_name")
        assert name_element.text == f"{name} {last_name}"
