from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pythonProject.pythonTestFramework.selenium_in_python.testshop.resources.pageObjects.login_page import \
    password_textfield, email_textfield


class LoginPage:
    submit_login_button = "//*[@id='submit-login']"

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def login(self, username, password):
        self.__driver.find_element(By.XPATH, email_textfield).send_keys(username)
        self.__driver.find_element(By.XPATH, password_textfield).send_keys(password)
        self.__driver.find_element(By.XPATH, self.submit_login_button).click()
