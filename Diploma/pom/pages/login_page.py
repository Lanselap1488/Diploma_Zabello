from ..pages.base_page import BasePage
from ..locators import login_locators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def find_text_enter_number(self):
        return self.find_element(login_locators.TEXT_ENTER_PHONE)

    def find_field_to_enter_phone(self):
        return self.find_element(login_locators.FIELD_TO_ENTER_PHONE)

    def press_enter(self):
        self.find_element(login_locators.ENTER_BUTTON).click()

    def find_text_to_enter_code(self):
        return self.find_element(login_locators.TEXT_ENTER_CODE)

    def find_error_incorrect_num(self):
        return self.find_element(login_locators.ERROR_INCORRECT_NUM)

    def find_error_incorrect_chars(self):
        return self.find_element(login_locators.ERROR_INCORRECT_CHARS)

    def enter_via_email(self):
        self.find_element(login_locators.ENTER_BY_POST).click()

    def enter_email_into_field(self, num):
        self.find_element(login_locators.EMAIL_FIELD).send_keys(num)

    def find_text_enter_via_email(self):
        return self.find_element(login_locators.TEXT_ENTER_MAIL)

    def click_to_ozon_id(self):
        self.find_element(login_locators.LINK_TO_OZON_ID).click()

    def check_text_ozon_id(self):
        return self.find_element(login_locators.LINK_TO_OZON_ID)

    def click_to_customers_support(self):
        self.find_element(login_locators.LINK_TO_CUSTOMERS_SUPPORT).click()

    def close_pop_up(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.find_element(login_locators.CLOSE_POP_UP).click()

    def check_text_customer_support(self):
        return self.find_element(login_locators.CUSTOMERS_SUPPORT_PAGE)





