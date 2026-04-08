import data.test_data as data

from pages.home_page import HomePage
from pages.tariff_page import TariffPage
from pages.payment_page import PaymentPage
from pages.order_page import OrderPage
from pages.ride_modal import RideModal


def test_1_set_route(driver):
    home = HomePage(driver)
    home.set_route(data.FROM_ADDRESS, data.TO_ADDRESS)
    assert True


def test_2_select_comfort(driver):
    tariff = TariffPage(driver)
    tariff.select_comfort()
    assert True


def test_3_enter_phone(driver):
    payment = PaymentPage(driver)
    payment.enter_phone(data.PHONE)
    assert True


def test_4_add_card(driver):
    payment = PaymentPage(driver)
    payment.add_card(data.CARD_NUMBER, data.CARD_CODE)
    assert True


def test_5_add_message(driver):
    order = OrderPage(driver)
    order.add_message(data.MESSAGE)
    assert True


def test_6_select_extras(driver):
    order = OrderPage(driver)
    order.select_blanket_and_tissues()
    assert True


def test_7_add_icecream(driver):
    order = OrderPage(driver)
    order.add_ice_creams(data.ICE_CREAM_COUNT)
    assert True


def test_8_confirm_order(driver):
    order = OrderPage(driver)
    order.confirm_order()
    assert True


def test_9_wait_driver(driver):
    ride = RideModal(driver)
    driver_info = ride.wait_for_driver()
    assert driver_info is not None