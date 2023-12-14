import pytest
from pythonProject.pythonTestFramework.selenium_in_python.testshop.helpers import DriverFactory, Browser
from pythonProject.pythonTestFramework.selenium_in_python.testshop.resources.pageObjects.homepage import homepage_url


@pytest.fixture(scope="function", autouse=True)
def driver():
    driver = DriverFactory.create_driver(Browser.CHROME)
    driver.get(homepage_url)
    driver.maximize_window()

    yield driver

    driver.quit()


