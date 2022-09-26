from ..pages.base_page import BasePage
from ..locators.search_res_locators import RES_TEXT, NO_RESULTS


class PageResultsSearch(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def find_item_result(self):
        return self.find_element(RES_TEXT)

    def there_is_no_results(self):
        return self.find_element(NO_RESULTS)