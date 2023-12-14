from selenium.webdriver.remote.webdriver import WebDriver

from pythonProject.pythonTestFramework.selenium_in_python.testshop.commons import Commons


class HomePage:
    search_button = "//form[@id='searchbox']//following-sibling::button[@type='submit']"
    signIn_button_homepage = "//*[@title='Log in to your customer account']"

    def __init__(self,driver: WebDriver):
        self.__driver = driver

    def open_login_page(self):
        commons = Commons(self.__driver)
        commons.click_element(self.signIn_button_homepage)
