import time
from selenium import webdriver
from pages.main_page import Main_page

def test_add_item_to_favourites():

    driver = webdriver.Chrome(executable_path=r'C:\\Users\\rdykin\\PycharmProjects\\resource\\chromedriver.exe')
    print('Начало теста')

    mp = Main_page(driver)
    mp.authorization()
    time.sleep(1.5)
    mp.favourites()
    driver.quit()

# python -m pytest -s -v test_add_to_favourites.py