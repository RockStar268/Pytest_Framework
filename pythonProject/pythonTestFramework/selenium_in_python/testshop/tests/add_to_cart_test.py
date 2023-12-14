from pythonProject.pythonTestFramework.selenium_in_python.testshop.commons import Commons
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages import HomePage, Validations
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages.AddToCart import AddToCart
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages.Search import Search
from pythonProject.pythonTestFramework.selenium_in_python.testshop.resources.pageObjects.add_to_cart_page import \
    proceed_checkout_button
from pythonProject.pythonTestFramework.selenium_in_python.testshop.resources.pageObjects.search_page import \
    validation_search_page


def test_add_to_cart(driver):
    search = Search(driver)
    validate = Validations(driver)
    add_to_cart = AddToCart(driver)
    commons = Commons(driver)

    mug = "//*[text()='Mug Today is a good day']"
    quantity_input = "//input[@id='quantity_wanted']"

    # ACT
    search.search_product("Mug")
    validate.element_displayed(validation_search_page)
    commons.click_element(mug)
    commons.clear_input_field(quantity_input)
    add_to_cart.add_item_to_cart(5)
    validate.product_successfully_added()
    commons.click_button(proceed_checkout_button)

