from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages import HomePage, Validations
import uuid
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages.CreateCustomer import CreateCustomer
from pythonProject.pythonTestFramework.selenium_in_python.testshop.resources.pageObjects.login_page import \
    sign_out_button


def test_create_account(driver):
    homepage = HomePage(driver)
    create_customer = CreateCustomer(driver)
    validation = Validations(driver)

    email = str(uuid.uuid4())[:10]

    homepage.open_login_page()
    create_customer.create_account(page="Create Customer", title="male", first_name="Test", last_name="Account", email=f"{email}@hotmail.com", dob="5/25/2000",
                                   password="TEST_TEST")
    validation.act_successfully_executed(sign_out_button)




