from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")

    ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'round') and contains(text(),'Pedir un taxi')]")

    def set_route(self, from_address, to_address):
        self.write(self.FROM_INPUT, from_address)
        self.write(self.TO_INPUT, to_address)
        self.click(self.ORDER_BUTTON)
        self.wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[text()='Comfort']")
    ))