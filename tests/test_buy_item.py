import time
from selenium import webdriver

from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.paints_page import Paints_page

def test_buying_item():

    driver = webdriver.Chrome(executable_path=r'C:\\Users\\rdykin\\PycharmProjects\\resource\\chromedriver.exe')
    print('Начало теста')

    mp = Main_page(driver)
    mp.driver_basic()
    mp.click_menu_catalog()

    time.sleep(1.5)
    mp.hover_menu_catalog()
    mp.hover_link_for_school()
    mp.hover_link_sewing()
    mp.hover_link_for_artists()
    mp.click_link_paints()

    pp = Paints_page(driver)
    pp.driver_basic()
    pp.add_item_into_cart()

    cp = Cart_page(driver)
    cp.driver_basic()
    cp.place_order()


    print('Завершение теста')
    time.sleep(3)
    driver.quit()

# python -m pytest -s -v test_buy_item.py