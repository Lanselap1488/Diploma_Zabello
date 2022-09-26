from ..pages.base_page import BasePage
from ..locators.Home_page_locators import LOGIN_BUTTON, SEARCH_FIELD, ACTION_POP_UP, \
    POP_UP_TEXT, POP_UP_WINDOW, SEARCH_CATEGORIES, CATEGORIES, SEARCH_CATEGORIES_POPUP, \
    SELECTED_CAT
from selenium.webdriver import Keys


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_home_page(self):
        self.driver.get('https://ozon.by/')

    def press_button_to_login(self):
        self.find_element(LOGIN_BUTTON).click()

    def find_something(self, item):
        self.find_element(SEARCH_FIELD).send_keys(item)
        self.find_element(SEARCH_FIELD).send_keys(Keys.ENTER)

    def move_to_action(self):
        self.move_to_element(self.find_element(ACTION_POP_UP))

    def find_pop_up_window(self):
        return self.find_element(POP_UP_WINDOW)

    def find_pop_up_text(self):
        return self.find_element(POP_UP_TEXT)

    def select_search_categories(self):
        self.find_element(SEARCH_CATEGORIES).click()

    def find_categories(self):
        return self.find_elements(CATEGORIES)

    def find_popup_with_categories(self):
        return self.find_element(SEARCH_CATEGORIES_POPUP)

    def get_selected_category(self):
        return self.find_element(SELECTED_CAT)







