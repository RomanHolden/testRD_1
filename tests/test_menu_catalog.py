import time
from selenium import webdriver

from pages.catalog_page import Catalog_page
from pages.knitting_page import Knitting_page
from pages.main_page import Main_page


def test_menu_analysis():

    driver = webdriver.Chrome(executable_path=r'C:\\Users\\rdykin\\PycharmProjects\\resource\\chromedriver.exe')
    print('Начало теста')

    mp = Main_page(driver)
    mp.driver_basic()
    time.sleep(1.5)
    mp.click_menu_catalog()
    time.sleep(1.5)
    cp = Catalog_page(driver)
    cp.tab_switching()
    mp.hover_menu_catalog()
    mp.hover_link_for_school()
    mp.hover_link_sewing()
    mp.hover_link_for_artists()
    mp.hover_link_stationery()
    mp.hover_link_knitting()
    mp.click_link_knitting()
    time.sleep(2)
    kp = Knitting_page(driver)
    kp.click_link_caskets()
    time.sleep(2)
    driver.back()
    print('Назад')
    time.sleep(1)
    driver.back()
    print('Назад')
    time.sleep(1)
    mp.hover_menu_catalog()
    time.sleep(1)
    mp.hover_link_sewing()
    time.sleep(1)
    mp.click_link_fabrics()

    print('Завершение теста')
    time.sleep(3)
    driver.quit()

# python -m pytest -s -v test_menu_catalog.py
