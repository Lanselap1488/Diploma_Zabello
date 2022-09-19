from selenium.webdriver.common.by import By


TEXT_ENTER_PHONE = (By.XPATH, '//div[contains(text(),"Введите номер телефона")]')
FIELD_TO_ENTER_PHONE = (By.CSS_SELECTOR, "input[type='phone']")
ENTER_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
TEXT_ENTER_CODE = (By.XPATH, '//div[contains(text(),"Введите код")]')
ERROR_INCORRECT_NUM = (By. XPATH, '//p[contains(text(),"Некорректный")]')
ERROR_INCORRECT_CHARS = (By. XPATH, '//p[contains(text(),"Заполните")]')
ENTER_BY_POST = (By.LINK_TEXT, 'Войти по почте')
EMAIL_FIELD = (By. CSS_SELECTOR, 'input[inputmode="email"]')
TEXT_ENTER_MAIL = (By.XPATH, '//div[contains(text(),"Войдите по почте")]')
ERROR_USER_NOT_FOUND = (By.XPATH, '//p[contains(text(),"Пользователь с указанным email не найден")]')
LINK_TO_OZON_ID = (By.LINK_TEXT, 'Что такое Ozon ID?')
LINK_TO_CUSTOMERS_SUPPORT = (By.LINK_TEXT, 'Помощь покупателю')
WHAT_IS_OZON_ID_TEXT = (By.ID, 'что-такое-ozon-id')
CLOSE_POP_UP = (By.XPATH, '//button[contains(text(),"Да, верно")]')
CUSTOMERS_SUPPORT_PAGE = (By.CLASS_NAME, 'page__wrapper')
