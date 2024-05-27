import time

import pytest
from selenium import webdriver

from page_objects.settings_page import SettingsPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    settings_page = SettingsPage(driver)
    settings_page.open()
    time.sleep(1)
    settings_page.delete_account()
    time.sleep(2)
