import pytest
from ..pages.home_page import HomePage
from ..pages.page_with_search_results import PageResultsSearch
from ..utils.data import TEXT1, CATEGORIES
import allure
from time import sleep


@allure.suite('From main page')
@allure.feature('Find item valid')
@pytest.mark.parametrize('item', ['кофеварка', 'телевизор', 'фен'])
def test_find_item_valid(driver, item):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.find_something(item)
    results = PageResultsSearch(driver)
    item_res = results.find_item_result()
    assert item in item_res.text and item_res.is_displayed()


@allure.suite('From main page')
@allure.feature('Find item invalid')
@pytest.mark.parametrize('item', ['jrhtker23', '()()(!@#4566&&^', '112324356543'])
def test_find_item_invalid(driver, item):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.find_something(item)
    results = PageResultsSearch(driver)
    item_res = results.there_is_no_results()
    assert item_res.is_displayed() and 'товаров сейчас нет' in item_res.text


@allure.suite('From main page')
@allure.feature('Pop up in main page')
def test_pop_up_is_open(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.move_to_action()
    window = home_page.find_pop_up_text()
    text_pop_up = home_page.find_pop_up_window()
    assert text_pop_up.is_displayed() and TEXT1 in window.text


@allure.suite('From main page')
@allure.feature('Window with list of categories opened')
def test_open_popup_with_categories(driver):
    home = HomePage(driver)
    home.open_home_page()
    home.select_search_categories()
    cat = home.find_popup_with_categories()
    assert cat.is_displayed()


@allure.suite('From main page')
@allure.feature('Select categories')
@pytest.mark.parametrize('num', [2, 11, 16, 27])
def test_select_category(driver, num):
    home = HomePage(driver)
    home.open_home_page()
    home.select_search_categories()
    categories = home.find_categories()
    categories[num].click()
    name = home.get_selected_category()
    assert name.text in CATEGORIES

