from selenium.webdriver.remote.webdriver import WebDriver

from pythonProject.pythonTestFramework.selenium_in_python.testshop.commons import Commons
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages import Validations


class Order:
    # input fields
    address_input_field = "//input[@name='address1']"
    city_input_field = "//input[@name='city']"
    zip_code_input_field = "//input[@name='postcode']"

    # dropdown
    country_dropdown = "//select[@name='id_country']"
    NL = "13"
    UK = "17"
    # buttons
    continue_button_address = "//button[@name='confirm-addresses']"
    continue_button_shipping_methods = "//button[@name='confirmDeliveryOption']"
    place_order_button = "//button[contains(text(), 'Place order')]"

    # radiobutton
    polteq_demo_shop_radiobutton = "//input[@id='delivery_option_1']"
    my_carrier_radiobutton = "//input[@id='delivery_option_2']"
    pay_by_check = "//input[@id='payment-option-1']"
    pay_by_wire = "//input[@id='payment-option-2']"

    # checkbox
    agree_TC_checkbox = "//input[@id='conditions_to_approve[terms-and-conditions]']"

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def fill_in_shipping_address(self, address_input, city_input, zip_code_input, country_dropdown):
        commons = Commons(self.__driver)


        commons.input_text(self.address_input_field, address_input)
        commons.input_text(self.city_input_field, city_input)
        commons.input_text(self.zip_code_input_field, zip_code_input)

        match country_dropdown:
            case "NL" | "Netherlands" | "the Netherlands":
                commons.select_dropdown_by_value(self.country_dropdown, value=self.NL)
            case "UK" | "United Kingdom" | "GB":
                commons.select_dropdown_by_value(self.country_dropdown, value=self.UK)

        commons.click_button(self.continue_button_address)

    def select_shipping_methods(self, type_shipping):
        commons = Commons(self.__driver)
        validation = Validations(self.__driver)

        match type_shipping:
            case "My Carrier":
                commons.click_button(self.my_carrier_radiobutton)
            case _:
                validation.default_option_is_selected(self.polteq_demo_shop_radiobutton)

        commons.click_button(self.continue_button_shipping_methods)

    def select_payment_method(self,type_payment):
        commons = Commons(self.__driver)
        type_payment = type_payment.lower()
        match type_payment:
            case "check":
                commons.click_button(self.pay_by_check)
            case "wire":
                commons.click_button(self.pay_by_wire)

        commons.click_button(self.agree_TC_checkbox)
        commons.click_button(self.place_order_button)
