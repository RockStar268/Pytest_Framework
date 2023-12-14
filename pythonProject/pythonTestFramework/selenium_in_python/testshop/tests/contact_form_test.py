from selenium.webdriver.common.by import By

from pythonProject.pythonTestFramework.selenium_in_python.testshop.commons.Commons import Commons
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages import Validations
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages.ContactForm import ContactForm
from pythonProject.pythonTestFramework.selenium_in_python.testshop.resources.pageObjects.contactForm import \
    validate_contactForm, webmaster, subject_dropdown, email_input_field_contact_form, message_input_field_contact_form, \
    submit_button_contact_form, submit_message_banner


def test_contact_form(driver):
    contact_form = ContactForm(driver)
    validation = Validations(driver)
    keyword = Commons(driver)

    contact_form.click_on_contact_us()
    validation.page_landed_successfully(validate_contactForm)

    # filling in form
    keyword.select_dropdown_by_value(element=subject_dropdown, value=webmaster)
    validation.assert_text(element=f"{subject_dropdown}/option[@value='{webmaster}']", expected_value="Webmaster")
    keyword.input_text(email_input_field_contact_form, "test@test.com")
    keyword.input_text(message_input_field_contact_form, "Hello World")
    keyword.click_button(submit_button_contact_form)

    # validation
    validation.assert_text(submit_message_banner, "Your message has been successfully sent to our team.")