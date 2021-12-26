import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox("/usr/local/bin")
    yield driver
    driver.quit()
