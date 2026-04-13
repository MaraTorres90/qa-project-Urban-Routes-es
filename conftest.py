import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from data import test_data as data


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")


    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(data.BASE_URL)

    yield driver

    driver.quit()
