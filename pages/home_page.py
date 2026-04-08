from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")

    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Pedir')]")

    def set_route(self, from_address, to_address):
        self.write(self.FROM_INPUT, from_address)
        self.write(self.TO_INPUT, to_address)

    def click_order(self):
        self.click(self.ORDER_BUTTON)