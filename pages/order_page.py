from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    MESSAGE_INPUT = (By.XPATH, "//input[@placeholder='Mensaje al conductor']")

    BLANKET_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and @name='blanket']")
    TISSUES_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and @name='tissues']")

    ICE_CREAM_PLUS = (By.XPATH, "//button[contains(@class,'plus')]")

    ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Pedir taxi')]")

    def add_message(self, message):
        self.write(self.MESSAGE_INPUT, message)

    def select_blanket_and_tissues(self):
        self.click(self.BLANKET_CHECKBOX)
        self.click(self.TISSUES_CHECKBOX)

    def add_ice_creams(self, quantity):
        for _ in range(quantity):
            self.click(self.ICE_CREAM_PLUS)

    def confirm_order(self):
        self.click(self.ORDER_BUTTON)