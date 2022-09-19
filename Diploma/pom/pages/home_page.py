from ..pages.base_page import BasePage
from ..locators.Home_page_locators import LOGIN_BUTTON



class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_home_page(self):
        self.driver.get('https://ozon.by/')

    def press_button_to_login(self):
        self.find_element(LOGIN_BUTTON).click()


