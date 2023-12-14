from selenium.webdriver.common.by import By

from pythonProject.pythonTestFramework.selenium_in_python.testshop.commons import Commons
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages import ContactForm


def test_navigate_back_and_forward(driver):
    contact_form = ContactForm(driver)
    navigation = Commons(driver)

    # act
    contact_form.click_on_contact_us()
    navigation.navigate_forward()
    navigation.navigate_back()
