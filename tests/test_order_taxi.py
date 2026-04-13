from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.tariff_page import TariffPage
from pages.payment_page import PaymentPage
from pages.order_page import OrderPage
from pages.ride_modal import RideModal

from data import test_data as data



def step_route(driver):
    home = HomePage(driver)
    home.set_route(data.FROM_ADDRESS, data.TO_ADDRESS)


def step_tariff(driver):
    step_route(driver)
    tariff = TariffPage(driver)
    tariff.select_comfort()


def step_phone(driver):
    step_tariff(driver)
    payment = PaymentPage(driver)
    payment.enter_phone(data.PHONE)


def step_card(driver):
    step_phone(driver)
    payment = PaymentPage(driver)
    payment.add_card(data.CARD_NUMBER, data.CARD_CODE)



def test_1_set_route(driver):
    step_route(driver)

    assert driver.find_element(By.ID, "from").get_attribute("value") == data.FROM_ADDRESS


def test_2_select_comfort(driver):
    step_tariff(driver)

    tariff = TariffPage(driver)
    assert tariff.comfort_rate_is_selected()


def test_3_enter_phone(driver):
    step_phone(driver)


    assert driver.find_element(By.CLASS_NAME, "np-text").text == data.PHONE


def test_4_add_card(driver):
    step_card(driver)

    assert driver.find_element(By.XPATH, "//div[contains(@class,'pp-button')]").is_displayed()


def test_5_add_message(driver):
    step_tariff(driver)

    order = OrderPage(driver)
    order.add_message(data.MESSAGE)

    assert driver.find_element(By.ID, "comment").get_attribute("value") == data.MESSAGE


def test_6_add_icecream(driver):
    step_tariff(driver)

    order = OrderPage(driver)
    order.select_extras(data.ICE_CREAM_COUNT)

    assert int(driver.find_element(By.XPATH, "//div[contains(@class,'counter-value')]").text) == data.ICE_CREAM_COUNT


def test_7_select_blanket_and_tissues(driver):
    step_tariff(driver)

    order = OrderPage(driver)
    order.select_extras(0)

    assert driver.find_element(By.CSS_SELECTOR, ".r-sw-container input").is_selected()


def test_8_search_taxi_modal(driver):
    step_card(driver)

    order = OrderPage(driver)
    order.confirm_order()

    ride = RideModal(driver)
    modal = ride.wait_for_search_modal()

    assert modal.is_displayed()


def test_9_wait_driver(driver):
    step_card(driver)

    order = OrderPage(driver)
    order.confirm_order()

    ride = RideModal(driver)
    driver_info = ride.wait_for_driver()

    assert driver_info.is_displayed()