from pages.home_page import HomePage
from pages.tariff_page import TariffPage
from pages.payment_page import PaymentPage
from pages.order_page import OrderPage
from pages.ride_modal import RideModal

from data import test_data as data



def test_1_set_route(driver):
    home = HomePage(driver)
    home.set_route(data.FROM_ADDRESS, data.TO_ADDRESS)



def test_2_select_comfort(driver):
    home = HomePage(driver)
    home.set_route(data.FROM_ADDRESS, data.TO_ADDRESS)

    tariff = TariffPage(driver)
    tariff.select_comfort()



def test_3_enter_phone(driver):
    home = HomePage(driver)
    home.set_route(data.FROM_ADDRESS, data.TO_ADDRESS)

    tariff = TariffPage(driver)
    tariff.select_comfort()

    payment = PaymentPage(driver)
    payment.enter_phone(data.PHONE)



def test_4_add_card(driver):
    home = HomePage(driver)
    home.set_route(data.FROM_ADDRESS, data.TO_ADDRESS)

    tariff = TariffPage(driver)
    tariff.select_comfort()

    payment = PaymentPage(driver)
    payment.add_card(data.CARD_NUMBER, data.CARD_CODE)


def test_5_add_message(driver):
    home = HomePage(driver)
    home.set_route(data.FROM_ADDRESS, data.TO_ADDRESS)

    tariff = TariffPage(driver)
    tariff.select_comfort()

    order = OrderPage(driver)
    order.add_message(data.MESSAGE)


def test_6_add_icecream(driver):
    home = HomePage(driver)
    home.set_route(data.FROM_ADDRESS, data.TO_ADDRESS)

    tariff = TariffPage(driver)
    tariff.select_comfort()

    order = OrderPage(driver)
    order.select_extras(data.ICE_CREAM_COUNT)


def test_7_select_blanket_and_tissues(driver):
    home = HomePage(driver)
    home.set_route(data.FROM_ADDRESS, data.TO_ADDRESS)

    tariff = TariffPage(driver)
    tariff.select_comfort()

    order = OrderPage(driver)
    order.select_extras(0)


def test_8_search_taxi_modal(driver):
    home = HomePage(driver)
    home.set_route(data.FROM_ADDRESS, data.TO_ADDRESS)

    tariff = TariffPage(driver)
    tariff.select_comfort()

    payment = PaymentPage(driver)
    payment.enter_phone(data.PHONE)
    payment.add_card(data.CARD_NUMBER, data.CARD_CODE)

    order = OrderPage(driver)
    order.confirm_order()

    ride = RideModal(driver)
    modal = ride.wait_for_search_modal()

    assert modal is not None

def test_9_wait_driver(driver):
    home = HomePage(driver)
    home.set_route(data.FROM_ADDRESS, data.TO_ADDRESS)

    tariff = TariffPage(driver)
    tariff.select_comfort()

    payment = PaymentPage(driver)
    payment.enter_phone(data.PHONE)
    payment.add_card(data.CARD_NUMBER, data.CARD_CODE)

    order = OrderPage(driver)
    order.confirm_order()

    ride = RideModal(driver)
    driver_info = ride.wait_for_driver()


    assert driver_info is not None