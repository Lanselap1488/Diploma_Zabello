from selenium.webdriver.common.by import By

LOGIN_BUTTON = (By.CSS_SELECTOR, 'div[data-widget="loginButton"]')
SEARCH = (By.CSS_SELECTOR, 'input[placeholder="Искать на Ozon"]')
SEARCH_FIELD = (By. CSS_SELECTOR, 'input[placeholder="Искать на Ozon"]')
ACTION_POP_UP = (By.CSS_SELECTOR, 'div[class="ui-k2 a7ga"]')
POP_UP_WINDOW = (By.CSS_SELECTOR, 'div[class="ui-k7"]')
POP_UP_TEXT = (By.XPATH, '//div[@class="ui-k7"]/div[1]')
SEARCH_CATEGORIES = (By. CSS_SELECTOR, 'span[title="Везде"]')
CATEGORIES = (By.CSS_SELECTOR, 'div[class="aak4"]')
SEARCH_CATEGORIES_POPUP = (By.CSS_SELECTOR, 'div[data-widget="searchContextPopup"]')
SELECTED_CAT = (By.CSS_SELECTOR, 'span[class="al8a tsBodyM a8al"]')