from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    MESSAGE_INPUT = (By.ID, "comment")

    BLANKET_SWITCH = (By.XPATH, "//span[contains(@class,'slider')]")
    ICE_CREAM_PLUS = (By.XPATH, "//div[contains(@class,'counter-plus')]")

    ORDER_BUTTON = (
        By.XPATH,
        "//button[.//span[contains(text(),'Pedir taxi')] or contains(.,'Pedir taxi')]"
    )

    DETAILS_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'order-button')]"
    )

    def add_message(self, message):
        element = self.wait.until(ec.element_to_be_clickable(self.MESSAGE_INPUT))
        element.clear()
        element.send_keys(message)

    def select_extras(self, icecream_count):
        self.wait.until(ec.element_to_be_clickable(self.BLANKET_SWITCH)).click()

        for _ in range(icecream_count):
            self.wait.until(ec.element_to_be_clickable(self.ICE_CREAM_PLUS)).click()

    def confirm_order(self):
        button = self.wait.until(
            ec.presence_of_element_located(self.ORDER_BUTTON)
        )


        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)


        self.wait.until(ec.visibility_of(button))


        self.driver.execute_script("arguments[0].click();", button)

        self.wait.until(
            ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'order')]"))
        )


    def open_details(self):
        button = self.wait.until(
            ec.presence_of_element_located(self.DETAILS_BUTTON)
        )

        self.driver.execute_script("arguments[0].click();", button)