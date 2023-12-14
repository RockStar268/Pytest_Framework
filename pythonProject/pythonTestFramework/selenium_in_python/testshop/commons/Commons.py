from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Commons:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def navigate_forward(self):
        self.__driver.forward()

    def navigate_back(self):
        self.__driver.back()

    def select_dropdown_by_value(self, element, value):
        select = Select(self.__driver.find_element(By.XPATH, element))
        select.select_by_value(value)

    def input_text(self, element, text):
        WebDriverWait(self.__driver, 20).until(ec.visibility_of_element_located((By.XPATH, element)))
        self.__driver.find_element(By.XPATH, element).send_keys(text)

    def clear_input_field(self, element):
        WebDriverWait(self.__driver, 20).until(ec.visibility_of_element_located((By.XPATH, element)))
        self.__driver.find_element(By.XPATH, element).clear()

    def click_button(self, element):
        #WebDriverWait(self.__driver, 20).until(ec.element_to_be_clickable((By.XPATH, element)))    this does not work..
        self.__driver.find_element(By.XPATH, element).click()

    def click_element(self, element):
        WebDriverWait(self.__driver, 20).until(ec.visibility_of_element_located((By.XPATH, element)))
        self.__driver.find_element(By.XPATH, element).click()
