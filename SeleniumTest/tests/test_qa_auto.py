import time

from page_objects.garage_page import GaragePage
from page_objects.home_page import HomePage
from page_objects.profile_page import ProfilePage
from page_objects.settings_page import SettingsPage


def test_simple_test(driver):
    name = "Gaview"
    last_name = "Mahat"

    wait_rate = 2
    home_page = HomePage(driver)

    home_page.open()

    login = f"{name}_{last_name}@my.mail"
    password = "1234567Aa_"

    home_page.create_user(name, last_name, login, password)
    # home_page.login(login, password)
    time.sleep(2 * wait_rate)

    profile = ProfilePage(driver)
    profile.open_from_home()
    time.sleep(1 * wait_rate)
    profile.check_user_name(name, last_name)

    garage = GaragePage(driver)
    garage.open()
    time.sleep(1 * wait_rate)
    mileage = 10
    garage.create_car("Ford", "Fusion", mileage)
    time.sleep(0.5 * wait_rate)
    garage.add_expense(mileage + 1, 1, 10)

    settings_page = SettingsPage(driver)
    settings_page.open()
    time.sleep(1)
    settings_page.delete_account()
    time.sleep(2)
