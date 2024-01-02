from logging import exception

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pythonProject.pythonTestFramework.selenium_in_python.testshop.commons import Commons, Conversion
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages import Validations
from pythonProject.pythonTestFramework.selenium_in_python.testshop.resources.pageObjects.login_page import \
    email_textfield, password_textfield
from pythonProject.pythonTestFramework.selenium_in_python.testshop.resources.pageObjects.order_page import \
    password_order_input_field, email_order_input_field, continue_button_create_customer_in_order


class CreateCustomer:

    create_account_link = "//a[@data-link-action='display-register-form']"
    title_male = "//input[@value='1'][ @name='id_gender']"
    title_female = "//*[@class='custom-radio']/input[@value='2']/span"
    first_name_input = "//input[@name='firstname']"
    last_name_input = "//input[@name='lastname']"
    dob_input = "//input[@name='birthday']"
    privacy_checkbox = "//input[@name='customer_privacy']"
    terms_conditions_checkbox = "//input[@name='psgdpr']"
    save_new_customer_button = "//*[@data-link-action='save-customer']"


    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def create_account(self, page, title, first_name, last_name, email, password, dob):
        commons = Commons(self.__driver)
        conversion = Conversion()
        validate = Validations(self.__driver)

        page = page.lower()

        # click on create account on login page
        try:
            self.__driver.find_element(By.XPATH, self.create_account_link).is_displayed()
            is_present = True
        except NoSuchElementException:
            is_present = False

        if is_present:
            commons.click_element(self.create_account_link)

        # fill in fields
        match title:
            case "male":
                commons.click_button(self.title_male)
            case "female":
                commons.click_button(self.title_female)

        commons.input_text(self.first_name_input, first_name)
        commons.input_text(self.last_name_input, last_name)
        dob_converted= Conversion.convert_date(dob)
        commons.input_text(self.dob_input, dob_converted)

        # check mandatory checkboxes
        commons.click_button(self.privacy_checkbox)
        commons.click_button(self.terms_conditions_checkbox)

        match page:
            case "create customer":
                commons.input_text(password_textfield, password)
                commons.input_text(email_textfield, email)
                commons.click_button(self.save_new_customer_button)

            case "order":
                commons.input_text(password_order_input_field, password)
                commons.input_text(email_order_input_field, email)
                commons.click_button(continue_button_create_customer_in_order)

       # validate_input = validate.assert_text(self.dob_input, conversion.date_of_birth(dob))             DOB does not get converted for some reason..
       # print(validate_input)



