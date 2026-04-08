from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RideModal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    DRIVER_INFO = (By.XPATH, "//div[contains(@class,'driver')]")

    def wait_for_driver(self):
        return self.wait.until(
            lambda driver: driver.find_element(*self.DRIVER_INFO)
        )