import time

from selenium.webdriver.common.by import By

from base.base_class import Base

'''Создание класса Catalog Page, дочернего по отношению к Base'''

class Catalog_page(Base):

    url = 'https://leonardo.ru/ishop/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators - здесь хранятся локаторы для работы с главной страницей

    tab_brands = '//a[@href="/ishop/brands/"]'
    tab_alphabet = '//a[@href="/ishop/alphabet/"]'
    tab_catalog = '//a[@data-toggle3="tab"]'

# Getters - здесь создаются методы получения доступа к нужным кнопкам главной страницы

    def get_tab_brands(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.tab_brands)))
        return self.driver.find_element(By.XPATH, self.tab_brands)

    def get_tab_alphabet(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.tab_alphabet)))
        return self.driver.find_element(By.XPATH, self.tab_alphabet)

    def get_tab_catalog(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.tab_catalog)))
        return self.driver.find_element(By.XPATH, self.tab_catalog)

# Actions - здесь создаются методы непосредственного взаимодействия с элементами главной страницы

    def click_tab_brands(self):
        self.get_tab_brands().click()
        print('Клик по вкладке "Бренды" сделан')
        self.assert_url('https://leonardo.ru/ishop/brands/')
        self.get_current_url()

    def click_tab_alphabet(self):
        self.get_tab_alphabet().click()
        print('Клик по вкладке "Поиск по алфавиту" сделан')
        self.assert_url('https://leonardo.ru/ishop/alphabet/')
        self.get_current_url()

    def click_tab_catalog(self):
        self.get_tab_catalog().click()
        print('Клик по вкладке "Каталог товаров" сделан')
        self.assert_url('https://leonardo.ru/ishop/')
        self.get_current_url()

# Scenario - здесь реализуется сценарий взаимодействия с главной страницей

    def tab_switching(self):
        time.sleep(1)
        self.click_tab_brands()
        time.sleep(1)
        self.click_tab_alphabet()
        time.sleep(1)
        self.click_tab_catalog()
        time.sleep(1)


    # python -m pytest -s -v
