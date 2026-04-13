from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from utils.helpers import retrieve_phone_code


class PaymentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    PHONE_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'np-button') and .//div[contains(text(),'Número de teléfono')]]"
    )

    PHONE_INPUT = (By.ID, "phone")

    NEXT_BUTTON = (By.XPATH, "//button[@type='submit' and text()='Siguiente']")

    CODE_INPUT = (By.ID, "code")

    CONFIRM_BUTTON = (By.XPATH, "//button[@type='submit' and text()='Confirmar']")



    PAYMENT_METHOD_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'pp-button') and .//div[text()='Método de pago']]"
    )

    ADD_CARD_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'pp-plus-container')]"
    )

    CARD_NUMBER = (By.ID, "number")

    CARD_CODE = (
        By.XPATH,
        "//div[contains(@class,'card-code-input')]//input"
    )

    ADD_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and text()='Agregar']"
    )

    CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'section-close')]"
    )

    def enter_phone(self, phone):


        button = self.wait.until(
            ec.presence_of_element_located(self.PHONE_BUTTON)
        )

        actions = ActionChains(self.driver)
        actions.move_to_element(button).pause(0.5).click().perform()


        inputs = self.wait.until(
            ec.presence_of_all_elements_located(self.PHONE_INPUT)
        )

        phone_filled = False

        for inp in inputs:
            if inp.is_displayed():


                self.wait.until(ec.element_to_be_clickable((By.ID, "phone")))


                self.driver.execute_script("arguments[0].click();", inp)

                inp.clear()
                inp.send_keys(phone)


                if inp.get_attribute("value") == phone:
                    phone_filled = True
                    break

        assert phone_filled, "No se pudo escribir el teléfono"


        next_btn = self.wait.until(
            ec.element_to_be_clickable(self.NEXT_BUTTON)
        )
        next_btn.click()


        code = retrieve_phone_code(self.driver)

        code_input = self.wait.until(
            ec.presence_of_element_located(self.CODE_INPUT)
        )


        self.wait.until(ec.visibility_of(code_input))


        self.driver.execute_script("arguments[0].click();", code_input)

        code_input.clear()
        code_input.send_keys(code)


        confirm_btn = self.wait.until(
            ec.element_to_be_clickable(self.CONFIRM_BUTTON)
        )
        confirm_btn.click()

    def add_card(self, number, code):

        button = self.wait.until(
            ec.presence_of_element_located(self.PAYMENT_METHOD_BUTTON)
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.wait.until(ec.visibility_of(button))
        self.driver.execute_script("arguments[0].click();", button)

        add_card = self.wait.until(
            ec.presence_of_element_located(self.ADD_CARD_BUTTON)
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_card)

        self.driver.execute_script("arguments[0].click();", add_card)


        self.wait.until(
            ec.visibility_of_element_located(self.CARD_NUMBER)
        )


        self.driver.find_element(*self.CARD_NUMBER).send_keys(number)

        card_code_input = self.driver.find_element(*self.CARD_CODE)
        card_code_input.send_keys(code)

        card_code_input.send_keys(Keys.TAB)

        add_btn = self.wait.until(
            ec.presence_of_element_located(self.ADD_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", add_btn)

        self.driver.execute_script("document.body.click();")

        self.wait.until(
            ec.invisibility_of_element_located(self.CARD_NUMBER)
        )

        import time
        time.sleep(1)