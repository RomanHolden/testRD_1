import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

'''Создание класса Books Page, дочернего по отношению к Base'''

class Books_page(Base):

    url = 'https://leonardo.ru/ishop/tree_1474576062/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators - здесь хранятся локаторы для работы с главной страницей

    link_house_design = '/html/body/div[2]/div/div[1]/div/ul/li[6]/a'
    filter_russia = '//label[@for="filtercheckhtstranapro:989"]'
    filter_tutorials = '//label[@for="filterchecknaznachenie:3347"]'
    filter_price_middle = '//label[@for="filtercheckprice:5"]'
    filter_price_middle_off = '//*[@id="category_itemslist"]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div[2]/a'
    clear_filters_button = '//*[@id="category_itemslist"]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/button'

# Getters - здесь создаются методы получения доступа к нужным кнопкам главной страницы

    def get_link_house_design(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_house_design)))
        #return self.driver.find_element(By.XPATH, self.link_house_design)

    def get_filter_russia(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.filter_russia)))
        #return self.driver.find_element(By.CSS_SELECTOR, self.filter_russia)

    def get_filter_tutorials(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.filter_tutorials)))
        #return self.driver.find_element(By.XPATH, self.filter_tutorials)

    def get_filter_price_middle(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.filter_price_middle)))
        #return self.driver.find_element(By.XPATH, self.filter_price_middle)

    def get_filter_price_middle_off(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.filter_price_middle_off)))
        #return self.driver.find_element(By.XPATH, self.filter_price_middle_off)

    def get_clear_filters_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.clear_filters_button)))
        #return self.driver.find_element(By.XPATH, self.clear_filters_button)

# Actions - здесь создаются методы непосредственного взаимодействия с элементами главной страницы

    def click_link_house_design(self):
        self.get_link_house_design().click()
        print('Клик по ссылке раздела книг для дизайна интерьера сделан')
        self.assert_url('https://leonardo.ru/ishop/tree_9538925112/')

    def click_filter_russia(self):
        self.get_filter_russia().click()
        print('Фильтр "Россия" включён')

    def click_filter_tutorials(self):
        self.get_filter_tutorials().click()
        print('Фильтр "Обучающие материалы" включён')

    def click_filter_price_middle(self):
        self.get_filter_price_middle().click()
        print('Фильтр "500 - 1000 руб." включён')


    def click_filter_price_middle_off(self):
        self.get_filter_price_middle_off().click()
        print('Фильтр "500 - 1000 руб." отключён')

    def click_clear_filters_button(self):
        self.get_clear_filters_button().click()
        print('Кнопка "СБРОСИТЬ ВСЕ" нажата')

    def driver_basic(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def look_for_element(self):
        x = len(self.driver.find_elements(By.CLASS_NAME, 'lasyloading'))
        print('Количество товаров: ', x)

# Scenario - здесь реализуется сценарий взаимодействия с главной страницей

    def filters_in_books(self):
        self.driver_basic()

        self.click_link_house_design()
        time.sleep(1)
        self.look_for_element() # считаем товары

        time.sleep(1)
        self.driver.execute_script('window.scrollTo(0,900)')
        print('Скролл вниз')

        time.sleep(1)
        self.click_filter_russia()
        time.sleep(1)
        self.look_for_element() # считаем товары

        time.sleep(1)
        self.driver.execute_script('window.scrollTo(0,400)')
        print('Скролл вверх')

        time.sleep(1)
        self.click_filter_tutorials()
        time.sleep(1)
        self.look_for_element()  # считаем товары

        time.sleep(1)
        self.click_filter_price_middle()
        time.sleep(1)
        self.look_for_element()  # считаем товары

        time.sleep(1)
        self.driver.execute_script('window.scrollTo(0,0)')
        print('Скролл вверх')

        time.sleep(1)
        self.click_filter_price_middle_off()
        time.sleep(1)
        self.look_for_element()  # считаем товары

        time.sleep(1)
        self.click_clear_filters_button()
        time.sleep(1)
        self.look_for_element()  # считаем элементы


# python -m pytest -s -v
