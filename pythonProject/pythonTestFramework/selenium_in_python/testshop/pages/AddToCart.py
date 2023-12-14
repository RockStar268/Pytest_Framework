from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pythonProject.pythonTestFramework.selenium_in_python.testshop.commons import Commons


class AddToCart:
    quantity_input = "//input[@id='quantity_wanted']"
    add_to_cart_button = "//button[@data-button-action='add-to-cart']"


    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def add_item_to_cart(self, quantity):
        self.__driver.find_element(By.XPATH, self.quantity_input).send_keys(quantity)
        self.__driver.find_element(By.XPATH, self.add_to_cart_button).click()
