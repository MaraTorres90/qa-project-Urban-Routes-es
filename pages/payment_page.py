from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PaymentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    PHONE_INPUT = (By.XPATH, "//input[@type='tel']")
    CARD_BUTTON = (By.XPATH, "//button[contains(text(),'Tarjeta')]")

    CARD_NUMBER = (By.XPATH, "//input[@name='number']")
    CARD_CODE = (By.XPATH, "//input[@name='code']")
    LINK_BUTTON = (By.XPATH, "//button[contains(text(),'Agregar')]")

    def enter_phone(self, phone):
        self.write(self.PHONE_INPUT, phone)

    def add_card(self, number, code):
        self.click(self.CARD_BUTTON)

        self.write(self.CARD_NUMBER, number)
        self.write(self.CARD_CODE, code)

        self.driver.find_element(*self.CARD_CODE).send_keys("\t")

        self.click(self.LINK_BUTTON)