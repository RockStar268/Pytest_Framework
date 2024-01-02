import uuid
from pythonProject.pythonTestFramework.selenium_in_python.testshop.commons import Commons
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages import Validations, AddToCart, HomePage
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages.CreateCustomer import CreateCustomer
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages.Order import Order
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages.Search import Search
from pythonProject.pythonTestFramework.selenium_in_python.testshop.resources.pageObjects.add_to_cart_page import \
    proceed_checkout_button
from pythonProject.pythonTestFramework.selenium_in_python.testshop.resources.pageObjects.order_page import \
    confirmed_order_validation
from pythonProject.pythonTestFramework.selenium_in_python.testshop.resources.pageObjects.search_page import \
    validation_search_page


def test_order(driver):

    search = Search(driver)
    validate = Validations(driver)
    add_to_cart = AddToCart(driver)
    commons = Commons(driver)
    homepage = HomePage(driver)
    create_customer = CreateCustomer(driver)
    validation = Validations(driver)
    order_page = Order(driver)

    mug = "//*[text()='Mug Today is a good day']"
    quantity_input = "//input[@id='quantity_wanted']"

    # ACT add item to cart
    search.search_product("Mug")
    validate.element_displayed(validation_search_page)
    commons.click_element(mug)
    commons.clear_input_field(quantity_input)
    add_to_cart.add_item_to_cart(5)
    validate.product_successfully_added()
    commons.click_button(proceed_checkout_button)

    # ACT click on proceed button on summary page
    commons.click_button(proceed_checkout_button)

    # ACT fill in user registration form
    email = str(uuid.uuid4())[:10]

    create_customer.create_account(page="Order", title="male", first_name="Test", last_name="Account", email=f"{email}@hotmail.com",
                                   dob="25-2-2000",
                                   password="TEST_TEST")

    # ACT fill in address details
    order_page.fill_in_shipping_address("Testing Lane", "Testing Village", "2525 AA", "NL")

    # ACT select shipping methods
    order_page.select_shipping_methods("Pick up in store")

    # ACT select payment method
    order_page.select_payment_method("Wire")

    # validation
    validation.assert_text(confirmed_order_validation, "Your order is confirmed")
