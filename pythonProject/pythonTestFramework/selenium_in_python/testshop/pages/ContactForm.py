from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ContactForm:
    contact_us = "//div[@id='contact-link']"

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def click_on_contact_us(self):
        self.__driver.find_element(By.XPATH, self.contact_us).click()

