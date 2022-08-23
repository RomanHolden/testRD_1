import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from base.base_class import Base

'''Создание класса Paints Page, дочернего по отношению к Base'''

class Paints_page(Base):

    url = 'https://leonardo.ru/ishop/tree_3780269209/'
    global value_item_price_clean

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators - здесь хранятся локаторы для работы с главной страницей

    item_1 = '//a[@href="/ishop/group_63445427434/"]'
    item_1_title = '//h1[@class="product-title-text"]'
    item_price = '//div[@class="actual-price"]'
    color_dropdown = '//a[@class="chosen-single chosen-default"]'
    color_dropdown_field = '//*[@id="colorselection_chosen"]/div/div/input'
    cart_button = '//button[@class="section-button sp_ordersbt"]'
    cart_icon = '//i[@class="shopping-cart"]'

# Getters - здесь создаются методы получения доступа к нужным кнопкам главной страницы

    def get_item_1(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.item_1)))
        return self.driver.find_element(By.XPATH, self.item_1)

    def get_item_1_title(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.item_1_title)))
        return self.driver.find_element(By.XPATH, self.item_1_title)

    def get_color_dropdown(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.color_dropdown)))
        return self.driver.find_element(By.XPATH, self.color_dropdown)

    def get_color_dropdown_field(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.color_dropdown_field)))
        return self.driver.find_element(By.XPATH, self.color_dropdown_field)

    def get_cart_button(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.cart_icon)))
        return self.driver.find_element(By.XPATH, self.cart_button)

    def get_cart_icon(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.cart_icon)))
        return self.driver.find_element(By.XPATH, self.cart_icon)

    def get_item_price(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.item_price)))
        value_item_price = self.driver.find_element(By.XPATH, self.item_price)
        value_item_price_filled = value_item_price.text
        value_item_price_clean = float(value_item_price_filled.replace('₽/шт', ''))
        print('Цена товара: ', value_item_price_clean)
        return value_item_price_clean


# Actions - здесь создаются методы непосредственного взаимодействия с элементами главной страницы

    def click_item_1(self):
        self.get_item_1().click()
        print('Клик по товару сделан')
        # self.assert_word(self.get_item_1_title(), 'Краска акриловая "VISTA-ARTISTA" idea декоративная глянцевая IGA-50 50 мл')
        # self.get_current_url()

    def click_color_dropdown(self):
        self.get_color_dropdown().click()
        print('Клик по выпадающему списку сделан')
        time.sleep(1)
        self.get_color_dropdown_field().send_keys('102')
        print('В поле введён номер цвета краски')
        time.sleep(1)
        self.get_color_dropdown_field().send_keys(Keys.RETURN)
        print('Значение поля сохранено')

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Кнопка "В корзину" нажата')

    def click_cart_icon(self):
        self.get_cart_icon().click()
        print('Иконка корзины вверху экрана нажата')

    def driver_basic(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

# Scenario - здесь реализуется сценарий взаимодействия с главной страницей

    def add_item_into_cart(self):
        time.sleep(0.2)
        self.click_item_1()
        time.sleep(0.2)
        self.get_item_price()
        self.click_color_dropdown()
        time.sleep(0.2)
        self.click_cart_button()
        time.sleep(0.2)
        self.click_cart_icon()
        self.assert_url('https://leonardo.ru/cart/')

    # python -m pytest -s -v
