from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TariffPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    COMFORT_TARIFF = (By.XPATH, "//div[contains(text(),'Comfort')]")

    def select_comfort(self):
        self.click(self.COMFORT_TARIFF)