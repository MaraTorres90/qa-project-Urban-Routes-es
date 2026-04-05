from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:

    # LOCATORS
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")

    COMFORT_TARIFF = (By.XPATH, "//div[contains(text(), 'Comfort')]")

    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.XPATH, "//button[contains(., 'Siguiente')]")

    CARD_BUTTON = (By.XPATH, "//button[contains(., 'Agregar tarjeta')]")
    CARD_NUMBER = (By.ID, "number")
    CARD_CODE = (By.ID, "code")
    LINK_BUTTON = (By.XPATH, "//button[contains(., 'Vincular')]")

    MESSAGE_INPUT = (By.ID, "comment")

    BLANKET_OPTION = (By.XPATH, "//span[contains(text(), 'Manta')]")
    TISSUE_OPTION = (By.XPATH, "//span[contains(text(), 'Pañuelos')]")

    ICE_CREAM_COUNTER = (By.XPATH, "//button[contains(@class, 'plus')]")

    ORDER_BUTTON = (By.XPATH, "//button[contains(., 'Pedir taxi')]")

    DRIVER_MODAL = (By.XPATH, "//div[contains(@class, 'order-details')]")

    # INIT
    def _init_(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # METHODS

    def set_route(self, from_addr, to_addr):
        self.wait.until(EC.visibility_of_element_located(self.FROM_INPUT)).send_keys(from_addr)
        self.driver.find_element(*self.TO_INPUT).send_keys(to_addr)

    def select_comfort_tariff(self):
        self.wait.until(EC.element_to_be_clickable(self.COMFORT_TARIFF)).click()

    def enter_phone(self, phone):
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def add_card(self, number, code):
        self.wait.until(EC.element_to_be_clickable(self.CARD_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.CARD_NUMBER)).send_keys(number)
        code_input = self.driver.find_element(*self.CARD_CODE)
        code_input.send_keys(code)

        # IMPORTANTE: quitar foco (TAB)
        code_input.send_keys(Keys.TAB)

        self.wait.until(EC.element_to_be_clickable(self.LINK_BUTTON)).click()

    def add_message(self, message):
        self.driver.find_element(*self.MESSAGE_INPUT).send_keys(message)

    def request_blanket_and_tissues(self):
        self.driver.find_element(*self.BLANKET_OPTION).click()
        self.driver.find_element(*self.TISSUE_OPTION).click()

    def order_ice_cream(self, quantity=2):
        for _ in range(quantity):
            self.driver.find_element(*self.ICE_CREAM_COUNTER).click()

    def order_taxi(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def wait_for_driver(self):
        self.wait.until(EC.visibility_of_element_located(self.DRIVER_MODAL))