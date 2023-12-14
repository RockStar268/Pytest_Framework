from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Validations:

    validate_succefully_added = "//h4[@id='myModalLabel']"

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def element_displayed(self, element):
        WebDriverWait(self.__driver, 20).until(ec.visibility_of_element_located((By.XPATH, element)))
        self.__driver.find_element(By.XPATH, element).is_displayed()

    def product_successfully_added(self):
        WebDriverWait(self.__driver, 20).until(ec.visibility_of_element_located((By.XPATH, self.validate_succefully_added)))
        self.__driver.find_element(By.XPATH, self.validate_succefully_added).is_displayed()

    def page_landed_successfully(self, element):
        WebDriverWait(self.__driver, 20).until(ec.visibility_of_element_located((By.XPATH, element)))
        self.__driver.find_element(By.XPATH, element).is_displayed()

    def act_successfully_executed(self, element):
        WebDriverWait(self.__driver, 20).until(ec.visibility_of_element_located((By.XPATH, element)))
        self.__driver.find_element(By.XPATH, element).is_displayed()

    def element_text_should_be(self, element):
        WebDriverWait(self.__driver, 20).until(ec.visibility_of_element_located((By.XPATH, element)))
        self.__driver.find_element(By.XPATH, element)

    def assert_text(self, element, expected_value):
        WebDriverWait(self.__driver, 20).until(ec.visibility_of_element_located((By.XPATH, element)))
        assert self.__driver.find_element(By.XPATH, element).text == expected_value, ("Actual value does not match "
                                                                                      "with expected value.")

    def default_option_is_selected(self, element):
        self.__driver.find_element(By.XPATH, element).is_selected()
