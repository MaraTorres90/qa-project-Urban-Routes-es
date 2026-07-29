"""Pruebas sencillas del proceso completo para pedir un taxi."""

import json
import time

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


def retrieve_phone_code(driver):
    """Obtiene de los registros del navegador el código enviado por Urban Routes."""
    for _ in range(10):
        for log in driver.get_log("performance"):
            message = json.loads(log["message"])["message"]
            if message["method"] != "Network.responseReceived":
                continue

            response = message["params"]["response"]
            if "/api/v1/number?number" not in response["url"]:
                continue

            try:
                body = driver.execute_cdp_cmd(
                    "Network.getResponseBody",
                    {"requestId": message["params"]["requestId"]},
                )
                return json.loads(body["body"])["code"]
            except Exception:
                pass

        time.sleep(1)

    raise Exception("No se pudo obtener el código del teléfono")


class UrbanRoutesPage:
    """Localizadores y acciones que se realizan en la página."""

    # Dirección
    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    OPEN_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'round') and contains(.,'Pedir un taxi')]",
    )

    # Tarifa
    COMFORT_TARIFF = (By.XPATH, "//div[text()='Comfort']")
    ACTIVE_COMFORT_TARIFF = (
        By.XPATH,
        "//div[contains(@class,'tcard') and contains(@class,'active')]"
        "[.//div[text()='Comfort']]",
    )

    # Teléfono
    PHONE_BUTTON = (By.CSS_SELECTOR, ".np-button")
    PHONE_INPUT = (By.ID, "phone")
    NEXT_BUTTON = (By.XPATH, "//button[@type='submit' and text()='Siguiente']")
    PHONE_CODE_INPUT = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, "//button[@type='submit' and text()='Confirmar']")
    SAVED_PHONE = (By.CLASS_NAME, "np-text")

    # Tarjeta
    PAYMENT_BUTTON = (By.CSS_SELECTOR, ".pp-button")
    ADD_CARD_BUTTON = (By.CSS_SELECTOR, ".pp-plus-container")
    CARD_NUMBER_INPUT = (By.ID, "number")
    CARD_CODE_INPUT = (By.CSS_SELECTOR, ".card-code-input input")
    ADD_BUTTON = (By.XPATH, "//button[@type='submit' and text()='Agregar']")
    CLOSE_MODAL_BUTTONS = (By.CSS_SELECTOR, "button.section-close")

    # Preferencias del viaje
    MESSAGE_INPUT = (By.ID, "comment")
    BLANKET_SWITCH = (
        By.XPATH,
        "//div[contains(@class,'r-sw-label') and text()='Manta y pañuelos']"
        "/following-sibling::div//span[contains(@class,'slider')]",
    )
    BLANKET_CHECKBOX = (
        By.XPATH,
        "//div[contains(@class,'r-sw-label') and text()='Manta y pañuelos']"
        "/following-sibling::div//input",
    )
    ICE_CREAM_PLUS = (
        By.XPATH,
        "//div[contains(@class,'r-counter-label') and text()='Helado']"
        "/following-sibling::div//div[contains(@class,'counter-plus')]",
    )
    ICE_CREAM_COUNT = (
        By.XPATH,
        "//div[contains(@class,'r-counter-label') and text()='Helado']"
        "/following-sibling::div//div[contains(@class,'counter-value')]",
    )

    # Pedido
    ORDER_TAXI_BUTTON = (
        By.CSS_SELECTOR,
        "button.smart-button",
    )
    ORDER_MODAL_TITLE = (By.CLASS_NAME, "order-header-title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def write(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(text)

    def set_route(self, from_address, to_address):
        self.write(self.FROM_INPUT, from_address)
        self.write(self.TO_INPUT, to_address)
        self.click(self.OPEN_ORDER_BUTTON)

    def select_comfort(self):
        comfort = self.wait.until(EC.visibility_of_element_located(self.COMFORT_TARIFF))
        self.driver.execute_script("arguments[0].click();", comfort)

    def enter_phone_number(self, phone_number):
        self.click(self.PHONE_BUTTON)
        self.write(self.PHONE_INPUT, phone_number)
        self.click(self.NEXT_BUTTON)

        confirmation_code = retrieve_phone_code(self.driver)
        self.write(self.PHONE_CODE_INPUT, confirmation_code)
        self.click(self.CONFIRM_BUTTON)

    def add_credit_card(self, card_number, card_code):
        self.click(self.PAYMENT_BUTTON)
        self.click(self.ADD_CARD_BUTTON)
        self.write(self.CARD_NUMBER_INPUT, card_number)

        code_field = self.wait.until(
            EC.visibility_of_element_located(self.CARD_CODE_INPUT)
        )
        code_field.send_keys(card_code)
        code_field.send_keys(Keys.TAB)  # Activa el botón Agregar.

        self.click(self.ADD_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(self.CARD_NUMBER_INPUT))

        # Al agregar la tarjeta vuelve a aparecer la ventana "Método de pago".
        # Buscamos la X que está visible y la cerramos para continuar el pedido.
        close_buttons = self.driver.find_elements(*self.CLOSE_MODAL_BUTTONS)
        for button in close_buttons:
            if button.is_displayed():
                button.click()
                break

        self.wait.until(
            EC.invisibility_of_element_located(self.ADD_CARD_BUTTON)
        )

    def write_message(self, message):
        self.write(self.MESSAGE_INPUT, message)

    def request_blanket_and_tissues(self):
        self.click(self.BLANKET_SWITCH)

    def request_two_ice_creams(self):
        self.click(self.ICE_CREAM_PLUS)
        self.click(self.ICE_CREAM_PLUS)

    def order_taxi(self):
        button = self.wait.until(EC.presence_of_element_located(self.ORDER_TAXI_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)

    def wait_for_driver_information(self):
        """Espera hasta que el título indique en cuántos minutos llegará."""
        return WebDriverWait(self.driver, 90).until(
            lambda driver: (
                title
                if (
                    (title := driver.find_element(*self.ORDER_MODAL_TITLE)).is_displayed()
                    and "min" in title.text
                )
                else False
            )
        )


class TestUrbanRoutes:
    """Cada prueba realiza un paso del mismo pedido."""

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_argument("--start-maximized")
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        # Selenium encuentra automáticamente el controlador de Chrome.
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(data.BASE_URL)
        cls.page = UrbanRoutesPage(cls.driver)

    def test_1_set_route(self):
        self.page.set_route(data.FROM_ADDRESS, data.TO_ADDRESS)
        assert self.driver.find_element(*self.page.FROM_INPUT).get_attribute(
            "value"
        ) == data.FROM_ADDRESS
        assert self.driver.find_element(*self.page.TO_INPUT).get_attribute(
            "value"
        ) == data.TO_ADDRESS

    def test_2_select_comfort(self):
        self.page.select_comfort()
        assert self.page.wait.until(
            EC.visibility_of_element_located(self.page.ACTIVE_COMFORT_TARIFF)
        )

    def test_3_enter_phone_number(self):
        self.page.enter_phone_number(data.PHONE_NUMBER)
        assert self.page.wait.until(
            EC.visibility_of_element_located(self.page.SAVED_PHONE)
        ).text == data.PHONE_NUMBER

    def test_4_add_credit_card(self):
        self.page.add_credit_card(data.CARD_NUMBER, data.CARD_CODE)
        assert self.driver.find_element(*self.page.PAYMENT_BUTTON).is_displayed()

    def test_5_write_message(self):
        self.page.write_message(data.MESSAGE_FOR_DRIVER)
        assert self.driver.find_element(*self.page.MESSAGE_INPUT).get_attribute(
            "value"
        ) == data.MESSAGE_FOR_DRIVER

    def test_6_request_blanket_and_tissues(self):
        self.page.request_blanket_and_tissues()
        assert self.driver.find_element(*self.page.BLANKET_CHECKBOX).is_selected()

    def test_7_request_two_ice_creams(self):
        self.page.request_two_ice_creams()
        assert self.driver.find_element(*self.page.ICE_CREAM_COUNT).text == "2"

    def test_8_order_taxi(self):
        self.page.order_taxi()
        modal_title = self.page.wait.until(
            EC.visibility_of_element_located(self.page.ORDER_MODAL_TITLE)
        )
        assert modal_title.is_displayed()

    # Esta prueba era opcional.
    def test_9_wait_for_driver(self):
        driver_title = self.page.wait_for_driver_information()
        assert "min" in driver_title.text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
