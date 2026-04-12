from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class RideModal(BasePage):

        def __init__(self, driver):
            super().__init__(driver)


        DRIVER_INFO = (
            By.XPATH,
            "//div[contains(@class,'order') and .//div[contains(@class,'driver')]]"
        )


        SEARCHING_MODAL = (
            By.XPATH,
            "//div[contains(text(),'Buscar') or contains(text(),'Buscando')]"
        )


        def wait_for_search_modal(self):
            return self.wait.until(
                ec.visibility_of_element_located(self.SEARCHING_MODAL)
            )

        def wait_for_driver(self):
            return self.wait.until(
                ec.visibility_of_element_located(self.DRIVER_INFO)
            )