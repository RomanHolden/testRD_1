import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_class import Base

'''Создание класса Main Page, дочернего по отношению к Base'''

class Main_page(Base):

    url = 'https://leonardo.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators - здесь хранятся локаторы для работы с главной страницей

    # MAIN
    favourites_icon = '//*[@id="header"]/div[2]/div[2]/div/div[3]/div/div[3]/div[2]/a/span'

    # AUTHORIZATION
    profile_icon = '//span[@class="header-links__label"]'
    mail_field = '//input[@id="login"]'
    pass_field = '//input[@id="password"]'
    enter_button = '//input[@value="Войти на сайт"]'
    title_registration = '/html/body/div[9]/div/h2'

    # CATALOG MAIN
    menu_catalog = '//a[@href="/ishop/"]'
    link_for_school = '//a[@href="/ishop/tree_9538924831/"]'
    link_sewing = '//a[@href="/ishop/tree_1454718762/"]'
    link_for_artists = '//a[@href="/ishop/tree_3812270609/"]'
    link_stationery = '//a[@href="/ishop/tree_3727030909/"]'
    link_knitting = '//a[@href="/ishop/tree_1444732062/"]'
    link_books = '//a[@href="/ishop/tree_1474576062/"]'

    # CATALOG SUB
    link_fabrics = '//a[@href="/ishop/tree_8433465762/"]'
    link_paints = '//a[@href="/ishop/tree_3780269209/"]'
    link_paper = '//a[@href="/ishop/tree_9538925442/"]'
    link_needles = '//a[@href="/ishop/tree_1452589662/"]'

    # QUICK LINKS
    link_educational_games = '//*[@id="header"]/div[4]/div/div/nav/a[1]'

    # OTHER
    item_star_favourites = '//*[@id="category_itemslist"]/div[2]/div[3]/div[2]/div[1]/button'
    product_in_favourites = '//div[@class="col-lg-4 product-item"]'


# Getters - здесь создаются методы получения доступа к нужным кнопкам главной страницы

    def get_profile_icon(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.profile_icon)))
        return self.driver.find_element(By.XPATH, self.profile_icon)

    def get_mail_field(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.mail_field)))
        return self.driver.find_element(By.XPATH, self.mail_field)

    def get_pass_field(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.pass_field)))
        return self.driver.find_element(By.XPATH, self.pass_field)

    def get_enter_button(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.enter_button)))
        return self.driver.find_element(By.XPATH, self.enter_button)

    def get_title_registration(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.title_registration)))
        return self.driver.find_element(By.XPATH, self.title_registration)

    def get_menu_catalog(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.menu_catalog)))
        return self.driver.find_element(By.XPATH, self.menu_catalog)

    def get_link_for_school(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_for_school)))
        return self.driver.find_element(By.XPATH, self.link_for_school)

    def get_link_sewing(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_sewing)))
        return self.driver.find_element(By.XPATH, self.link_sewing)

    def get_link_for_artists(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_for_artists)))
        return self.driver.find_element(By.XPATH, self.link_for_artists)

    def get_link_stationery(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_stationery)))
        return self.driver.find_element(By.XPATH, self.link_stationery)

    def get_link_knitting(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_knitting)))
        return self.driver.find_element(By.XPATH, self.link_knitting)

    def get_link_fabrics(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_fabrics)))
        return self.driver.find_element(By.XPATH, self.link_fabrics)

    def get_link_paints(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_paints)))
        return self.driver.find_element(By.XPATH, self.link_paints)

    def get_link_paper(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_paper)))
        return self.driver.find_element(By.XPATH, self.link_paper)

    def get_link_needles(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_needles)))
        return self.driver.find_element(By.XPATH, self.link_needles)

    def get_link_books(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_books)))
        return self.driver.find_element(By.XPATH, self.link_books)

    def get_favourites_icon(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.favourites_icon)))
        return self.driver.find_element(By.XPATH, self.favourites_icon)

    def get_link_educational_games(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_educational_games)))
        return self.driver.find_element(By.XPATH, self.link_educational_games)

    def get_item_star_favourites(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.item_star_favourites)))
        return self.driver.find_element(By.XPATH, self.item_star_favourites)

    def get_product_in_favourites(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product_in_favourites)))
        return self.driver.find_element(By.XPATH, self.product_in_favourites)


# Actions - здесь создаются методы непосредственного взаимодействия с элементами главной страницы

    def click_profile_icon(self):
        self.get_profile_icon().click()
        print('Иконка входа в профиль нажата')

    def input_mail_field(self):
        self.get_mail_field().send_keys('roman_pr@inbox.ru')
        print('Поле логина заполнено')

    def input_pass_field(self):
        self.get_pass_field().send_keys('testSELENIUM2022')
        print('Поле пароля заполнено')

    def click_enter_button(self):
        self.get_enter_button().click()
        print('Кнопка входа нажата')

    def click_favourites_icon(self):
        self.get_favourites_icon().click()
        print('Иконка "Избранное" нажата')

    def click_menu_catalog(self):
        self.get_menu_catalog().click()
        print('Меню каталога открыто')
        self.assert_url('https://leonardo.ru/ishop/')


    def click_link_knitting(self):
        self.get_link_knitting().click()
        print('Клик по ссылке товаров для вязания сделан')
        self.assert_url('https://leonardo.ru/ishop/tree_1444732062/')

    def click_link_sewing(self):
        self.get_link_sewing().click()
        print('Клик по ссылке товаров для шитья сделан')
        self.assert_url('https://leonardo.ru/ishop/tree_1454718762/')

    def click_link_fabrics(self):
        self.get_link_fabrics().click()
        print('Клик по ссылке раздела тканей сделан')
        self.assert_url('https://leonardo.ru/ishop/tree_8433465762/')

    def click_link_paints(self):
        self.get_link_paints().click()
        print('Клик по ссылке раздела красок сделан')
        self.assert_url('https://leonardo.ru/ishop/tree_3780269209/')

    def click_link_educational_games(self):
        self.get_link_educational_games().click()
        print('Клик по ссылке раздела развивающих игр сделан')
        self.assert_url('https://leonardo.ru/ishop/tree_3811874809/')

    def click_link_books(self):
        self.get_link_books().click()
        print('Клик по ссылке раздела книг сделан')
        self.assert_url('https://leonardo.ru/ishop/tree_1474576062/')

    def click_item_star_favourites(self):
        self.get_item_star_favourites().click()
        print('Клик по звёздочке "Избранное" на карточке товара сделан')


    def hover_menu_catalog(self):
        ActionChains(self.driver)\
            .move_to_element(self.get_menu_catalog())\
            .perform()
        time.sleep(1)
        print('Курсор наведён на меню каталога')

    def hover_link_for_school(self):
        ActionChains(self.driver)\
            .move_to_element(self.get_link_for_school())\
            .perform()
        time.sleep(0.5)
        print('Курсор наведён на раздел товаров к школе')
        try:
            self.assert_word(self.get_link_fabrics(), 'Ткани')
        except AssertionError:
            print('Всплывающих списков не обнаружено (соответствует требованиям)')

    def hover_link_sewing(self):
        ActionChains(self.driver)\
            .move_to_element(self.get_link_sewing())\
            .perform()
        time.sleep(0.5)
        print('Курсор наведён на раздел товаров для шитья')
        try:
            self.assert_word(self.get_link_fabrics(), 'Ткани')
        except AssertionError:
            print('Всплывающий список не соответствует требованиям и/или отсутствует')

    def hover_link_for_artists(self):
        ActionChains(self.driver)\
            .move_to_element(self.get_link_for_artists())\
            .perform()
        time.sleep(0.5)
        print('Курсор наведён на раздел товаров для художников')
        # try:
        #     self.assert_word(self.get_link_paints(), 'Краски')
        # except AssertionError:
        #     print('Всплывающий список не соответствует требованиям и/или отсутствует')


    def hover_link_stationery(self):
        ActionChains(self.driver)\
            .move_to_element(self.get_link_stationery())\
            .perform()
        time.sleep(1)
        print('Курсор наведён на раздел канцелярских товаров')
        try:
            self.assert_word(self.get_link_paper(), 'Бумажная продукция')
        except AssertionError:
            print('Всплывающий список не соответствует требованиям и/или отсутствует')

    def hover_link_knitting(self):
        ActionChains(self.driver)\
            .move_to_element(self.get_link_knitting())\
            .perform()
        time.sleep(1)
        print('Курсор наведён на раздел товаров для вязания')
        try:
            self.assert_word(self.get_link_needles(), 'Спицы')
        except AssertionError:
            print('Всплывающий список не соответствует требованиям и/или отсутствует')


    def driver_basic(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

# Scenario - здесь реализуется сценарий взаимодействия с главной страницей

    def authorization(self):
        self.driver_basic()
        time.sleep(0.3)
        self.click_profile_icon()
        time.sleep(0.3)
        self.input_mail_field()
        time.sleep(0.3)
        self.input_pass_field()
        time.sleep(0.3)
        self.click_enter_button()
        time.sleep(3)
        self.click_profile_icon()
        time.sleep(0.3)
        self.assert_url('https://leonardo.ru/profile/')

    def favourites(self):
        self.driver_basic()
        self.click_favourites_icon()
        time.sleep(2)
        self.assert_url('https://leonardo.ru/profile/wishlist/')
        self.click_link_educational_games()
        time.sleep(2)
        self.click_item_star_favourites()
        time.sleep(2)
        self.get_screenshot()
        self.click_favourites_icon()
        time.sleep(2)
        self.get_product_in_favourites()
        self.get_screenshot()
        print('Добавленный товар обнаружен на странице "Избранное"')
        print('Завершение теста')
        time.sleep(2)







    # python -m pytest -s -v
