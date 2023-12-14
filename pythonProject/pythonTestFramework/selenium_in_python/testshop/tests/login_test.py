from selenium.webdriver.common.by import By
from pythonTestFramework.selenium_in_python.testshop.pages import HomePage
from pythonTestFramework.selenium_in_python.testshop.pages.LoginPage import LoginPage
from pythonTestFramework.selenium_in_python.testshop.resources.pageObjects.login_page import login_page_URL, validate_successful_login

from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages import Validations


def test_login(driver):

    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    login_successful = Validations(driver)

    home_page.open_login_page()

    # act
    current_url = driver.current_url
    assert current_url == login_page_URL

    login_page.login("tester@test.com", "1qazxsw2")
    # validate
    login_successful.act_successfully_executed(validate_successful_login)
