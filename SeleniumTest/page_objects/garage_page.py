import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class GaragePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get("https://qauto2.forstudy.space/panel/garage")

    def create_car(self, brand, model, mileage):
        self._driver.find_element(By.XPATH, "//button[text()='Add car']").click()
        time.sleep(1)

        car_brand = Select(self._driver.find_element(By.ID, "addCarBrand"))
        car_brand.select_by_visible_text(brand)
        time.sleep(1)

        car_model = Select(self._driver.find_element(By.ID, "addCarModel"))
        car_model.select_by_visible_text(model)

        self._driver.find_element(By.ID, "addCarMileage").send_keys(str(mileage))
        self._driver.find_element(By.XPATH, "//button[text()='Add']").click()

    def add_expense(self, mileage, fuel, total_cost):
        self._driver.find_element(By.XPATH, "//button[text()='Add fuel expense']").click()
        time.sleep(0.2)

        self._driver.find_element(By.ID, "addExpenseMileage").clear()
        self._driver.find_element(By.ID, "addExpenseMileage").send_keys(str(mileage))

        self._driver.find_element(By.ID, "addExpenseLiters").send_keys(fuel)
        self._driver.find_element(By.ID, "addExpenseTotalCost").send_keys(total_cost)

        self._driver.find_element(By.XPATH, "//button[text()='Add']").click()

