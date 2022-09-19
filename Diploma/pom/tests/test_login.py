from ..pages.home_page import HomePage
from ..pages.login_page import LoginPage
import pytest
from ..utils.data import PHONES, INVALID_NUM, INVALID_CHARS
from time import sleep


def test_press_button_login(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.press_button_to_login()
    login_page = LoginPage(driver)
    text_login = login_page.find_text_enter_number()
    assert text_login.is_displayed() and "Введите номер телефона" in text_login.text


@pytest.mark.parametrize('num', PHONES)
def test_enter_valid_phone(driver, num):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.press_button_to_login()
    login_page = LoginPage(driver)
    login_page.find_field_to_enter_phone().send_keys(num)
    login_page.press_enter()
    code = login_page.find_text_to_enter_code()
    assert code.is_displayed() and "Введите код" in code.text


@pytest.mark.parametrize('num', INVALID_NUM)
def test_enter_invalid_phone_numbers(driver, num):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.press_button_to_login()
    login_page = LoginPage(driver)
    login_page.find_field_to_enter_phone().send_keys(num)
    login_page.press_enter()
    error = login_page.find_error_incorrect_num()
    assert error.is_displayed and 'Некорректный формат телефона' in error.text


@pytest.mark.parametrize('num', INVALID_CHARS)
def test_enter_invalid_phone_empty(driver, num):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.press_button_to_login()
    login_page = LoginPage(driver)
    login_page.find_field_to_enter_phone().send_keys(num)
    login_page.press_enter()
    error = login_page.find_error_incorrect_chars()
    assert error.is_displayed and 'Заполните телефон' in error.text


def test_enter_via_email_is_open(driver):
    home = HomePage(driver)
    home.open_home_page()
    home.press_button_to_login()
    login_page = LoginPage(driver)
    login_page.enter_via_email()
    mail = login_page.find_text_enter_via_email()
    assert mail.is_displayed() and "Войдите по почте" in mail.text


def test_switch_to_ozon_id_page(driver):
    home = HomePage(driver)
    home.open_home_page()
    home.press_button_to_login()
    login_page = LoginPage(driver)
    login_page.click_to_ozon_id()
    ozon_id = login_page.check_text_ozon_id()
    assert ozon_id.is_displayed() and 'Что такое Ozon ID' in ozon_id.text


def test_switch_to_customer_support_page(driver):
    home = HomePage(driver)
    home.open_home_page()
    home.press_button_to_login()
    login_page = LoginPage(driver)
    login_page.click_to_customers_support()
    login_page.close_pop_up()
    support = login_page.check_text_customer_support()
    assert support.is_displayed() and 'Главная' in support.text



# @pytest.mark.parametrize('mail', MAIL_UNREGISTERED)
# def test_login_via_mail_registered(driver, mail):
#     home = HomePage(driver)
#     home.open_home_page()
#     home.press_button_to_login()
#     login_page = LoginPage(driver)
#     login_page.enter_via_email()
#     login_page.enter_email_into_field(mail)
#     login_page.press_enter()
#     error = login_page.error_unregistered_mail()
#     assert error.is_displayed()

















