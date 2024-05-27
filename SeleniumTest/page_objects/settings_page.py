import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class SettingsPage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get("https://qauto2.forstudy.space/panel/settings")

    def delete_account(self):
        # self._driver.find_element(By.CLASS_NAME, "btn-danger-bg").click()
        self._driver.find_element(By.XPATH, "//button[text()='Remove my account']").click()
        time.sleep(0.2)
        self._driver.find_element(By.XPATH, "//button[text()='Remove']").click()
