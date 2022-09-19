from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture(scope='function')
def driver():
    serv = Service(executable_path='C:\\chromedriver\\chromedriver.exe')
    opt = Options()
    opt.add_argument('--start-maximized')
    driver_chrome = webdriver.Chrome(options=opt, service=serv)
    driver_chrome.implicitly_wait(10)
    yield driver_chrome
    driver_chrome.quit()
