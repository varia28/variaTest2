import time

from page_objects.garage_page import GaragePage
from page_objects.home_page import HomePage
from page_objects.profile_page import ProfilePage

name = "Gaview"
last_name = "Mahat"


def test_simple_test(driver):
    wait_rate = 2
    home_page = HomePage(driver)

    home_page.open()

    home_page.create_user(name, last_name)
    # home_page.login()
    time.sleep(2 * wait_rate)

    profile = ProfilePage(driver)
    profile.open_from_home()
    time.sleep(1 * wait_rate)
    profile.check_user_name(name, last_name)

    garage = GaragePage(driver)
    garage.open()
    time.sleep(1 * wait_rate)
    garage.create_car()
    time.sleep(0.5 * wait_rate)
    garage.add_expense()