import pytest
from selenium import webdriver
import data

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(data.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()