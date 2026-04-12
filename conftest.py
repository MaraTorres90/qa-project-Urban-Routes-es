import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")


    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://cnt-c198b977-7488-46be-9e6c-267aab8f95b4.containerhub.tripleten-services.com?lng=es")

    yield driver

    driver.quit()
