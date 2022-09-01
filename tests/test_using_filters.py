import time
from selenium import webdriver

from pages.books_page import Books_page
from pages.main_page import Main_page


def test_filters():
    '''В этом тесте мы проверяем возможность использования фильтров при покупке товара'''
    driver = webdriver.Chrome(executable_path=r'C:\\Users\\rdykin\\PycharmProjects\\resource\\chromedriver.exe')
    print('Начало теста')

    mp = Main_page(driver)
    mp.driver_basic()
    mp.click_menu_catalog()

    time.sleep(1)
    mp.hover_menu_catalog()
    mp.click_link_books()

    bp = Books_page(driver)
    bp.filters_in_books()

    print('Завершение теста')
    time.sleep(2)
    driver.quit()

# python -m pytest -s -v test_using_filters.py