
from selenium import webdriver
from pages.main_page import Main_page
from pages.profile_page import Profile_page


def test_profile():

    driver = webdriver.Chrome(executable_path=r'C:\\Users\\rdykin\\PycharmProjects\\resource\\chromedriver.exe')
    print('Начало теста')

    mp = Main_page(driver)
    mp.authorization()

    prp = Profile_page(driver)
    prp.editing_profile()

    driver.quit()

# python -m pytest -s -v test_profile_sections.py