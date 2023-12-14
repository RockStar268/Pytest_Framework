from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Search:
    product_search_homepage = "//input[@placeholder='Search our catalog']"
    submit_button_searchField_homepage = "//button[@type='submit']"
    results_search_output = "//h2[@itemprop='name']"
     # "//div[@class ='products row']"


    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def search_product(self, product):
        self.__driver.find_element(By.XPATH, self.product_search_homepage).send_keys(product)
        self.__driver.find_element(By.XPATH, self.submit_button_searchField_homepage).click()

    def retrieve_search_result_items(self):
        list_items = []

        try:
            search_results = self.__driver.find_elements(By.XPATH, self.results_search_output)

            if search_results:
                for result in search_results:
                    list_items.append(result.text)
        except NoSuchElementException:
            is_search_results_returned = False
            assert not is_search_results_returned, "Your search input returned with no items!"

        print(list_items)
