from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._login = None
        self._pass = "1234567Aa_"

    def open(self):
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")

    def create_user(self, name, last_name):
        driver = self._driver

        self._login = f"{name}_{last_name}@mah.mah"

        driver.find_element(By.XPATH, "//button[contains(.,'Sign up')]").click()
        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(name)
        driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys(last_name)
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(self._login)
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(self._pass)
        driver.find_element(By.XPATH, "//input[@name='repeatPassword']").send_keys(self._pass)
        driver.find_element(By.XPATH, "//button[contains(.,'Register')]").click()

    def login(self):
        driver = self._driver

        driver.find_element(By.CLASS_NAME, "header_signin").click()
        driver.find_element(By.ID, "signinEmail").send_keys(self._login)
        driver.find_element(By.ID, "signinPassword").send_keys(self._pass)
        driver.find_element(By.XPATH, "//button[contains(.,'Login')]").click()
