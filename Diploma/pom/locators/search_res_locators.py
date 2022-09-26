from selenium.webdriver.common.by import By

RES_TEXT = (By.XPATH, '//div[@class="ala2"]/strong')
NO_RESULTS = (By.XPATH, '//div[contains(text(),"Простите, по вашему запросу товаров сейчас нет.")]')
