from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def open(self):
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")

    def create_user(self, name, last_name, login, password):
        self._driver.find_element(By.XPATH, "//button[contains(.,'Sign up')]").click()
        self._driver.find_element(By.XPATH, "//input[@name='name']").send_keys(name)
        self._driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys(last_name)
        self._driver.find_element(By.XPATH, "//input[@name='email']").send_keys(login)
        self._driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        self._driver.find_element(By.XPATH, "//input[@name='repeatPassword']").send_keys(password)
        self._driver.find_element(By.XPATH, "//button[contains(.,'Register')]").click()

    def login(self, login, password):
        self._driver.find_element(By.CLASS_NAME, "header_signin").click()
        self._driver.find_element(By.ID, "signinEmail").send_keys(login)
        self._driver.find_element(By.ID, "signinPassword").send_keys(password)
        self._driver.find_element(By.XPATH, "//button[contains(.,'Login')]").click()
