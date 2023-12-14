from pythonProject.pythonTestFramework.selenium_in_python.testshop.commons import Commons
from pythonProject.pythonTestFramework.selenium_in_python.testshop.pages.Search import Search


def test_search(driver):
    keywords = Commons(driver)
    search_page = Search(driver)

    # search for mug
    search_page.search_product("Mug")
    search_page.retrieve_search_result_items()

