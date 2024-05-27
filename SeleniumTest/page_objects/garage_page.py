import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class GaragePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._mileage = 11

    def open(self):
        self._driver.get("https://qauto2.forstudy.space/panel/garage")

    def create_car(self):
        driver = self._driver
        driver.find_element(By.XPATH, "//button[text()='Add car']").click()
        time.sleep(1)
        car_brand = Select(driver.find_element(By.ID, "addCarBrand"))
        car_brand.select_by_visible_text("Ford")
        time.sleep(1)
        car_model = Select(driver.find_element(By.ID, "addCarModel"))
        car_model.select_by_visible_text("Fusion")
        driver.find_element(By.ID, "addCarMileage").send_keys(str(self._mileage))
        driver.find_element(By.XPATH, "//button[text()='Add']").click()

    def add_expense(self):
        driver = self._driver
        driver.find_element(By.XPATH, "//button[text()='Add fuel expense']").click()
        time.sleep(0.2)

        driver.find_element(By.ID, "addExpenseMileage").clear()
        driver.find_element(By.ID, "addExpenseMileage").send_keys(str(self._mileage + 1))

        driver.find_element(By.ID, "addExpenseLiters").send_keys("1")
        driver.find_element(By.ID, "addExpenseTotalCost").send_keys("2")

        driver.find_element(By.XPATH, "//button[text()='Add']").click()

