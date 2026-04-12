from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TariffPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    COMFORT_TARIFF = (By.XPATH, "//div[text()='Comfort']")

    def select_comfort(self):
        element = self.wait.until(
            ec.visibility_of_element_located(self.COMFORT_TARIFF)
        )

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        self.driver.execute_script("arguments[0].click();", element)

        import time
        time.sleep(1)

        self.wait.until(
            ec.presence_of_element_located(
                (By.XPATH, "//div[contains(@class,'tcard active')]//div[text()='Comfort']")
            )
        )