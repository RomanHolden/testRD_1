import time

from selenium.webdriver.common.by import By

from base.base_class import Base
from utilities.logger import Logger

'''Создание класса Cart Page, дочернего по отношению к Base'''

class Cart_page(Base):

    url = 'https://leonardo.ru/cart/'
    global value_item_price_clean
    global value_price_in_cart_1_clean

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators - здесь хранятся локаторы для работы с главной страницей

    cart_icon = '//i[@class="shopping-cart"]'

    # Main
    place_order_button = '//a[@class="gotocheckout btn-main btn-cart "]'
    item_title_in_cart = '/html/body/div[2]/div[4]/div[1]/div/div/div[2]/div/div[1]/div[1]/a'
    plus_button = '/html/body/div[2]/div[4]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/span/a[1]'
    minus_button = '/html/body/div[2]/div[4]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/span/a[2]'
    price_in_cart_1 = '/html/body/div[2]/div[4]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/b'
    price_in_cart_2 = '//span[@class="amount-excl-discounts"]'
    price_in_cart_full = '//span[@class="cartfullprice"]'
    text_under_quantity = '//div[@class="zakazblock cart-params-info"]'
    text_under_sum = '/html/body/div[2]/div[4]/div[2]/div/div[2]/div[2]/div/div[3]'
    agreement_in_cart = '/html/body/div[2]/div[4]/div[2]/div/div[4]/div/div/label'
    basket_icon = '//i[@class="remove-obj"]'
    favourites_option = '//span[@class="wishlist_text"]'
    empty_cart_text = '//p[@class="empty-shopping-cart-text"]'

    # After click "Place order"
    delivery_title = '//*[@id="order_form"]/fieldset/div[2]/div[3]/div[5]/span'
    payment_methods = '//*[@id="order_form"]/fieldset/div[2]/div[4]/span[1]'

# Getters - здесь создаются методы получения доступа к нужным кнопкам главной страницы

    def get_place_order_button(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.place_order_button)))
        return self.driver.find_element(By.XPATH, self.place_order_button)

    def get_item_title_in_cart(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.item_title_in_cart)))
        return self.driver.find_element(By.XPATH, self.item_title_in_cart)

    def get_plus_button(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.plus_button)))
        return self.driver.find_element(By.XPATH, self.plus_button)

    def get_minus_button(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.minus_button)))
        return self.driver.find_element(By.XPATH, self.minus_button)

    def get_price_in_cart_1(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.price_in_cart_1)))
        value_price_in_cart_1 = self.driver.find_element(By.XPATH, self.price_in_cart_1)
        value_price_in_cart_1_filled = value_price_in_cart_1.text
        value_price_in_cart_1_clean = float(value_price_in_cart_1_filled.replace('₽', ''))
        print('Цена товара в корзине: ', value_price_in_cart_1_clean)
        return value_price_in_cart_1_clean

    def get_price_in_cart_2(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.price_in_cart_1)))
        value_price_in_cart_2 = self.driver.find_element(By.XPATH, self.price_in_cart_2)
        value_price_in_cart_2_filled = value_price_in_cart_2.text
        return value_price_in_cart_2_filled

    def get_price_in_cart_full(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.price_in_cart_1)))
        value_price_in_cart_full = self.driver.find_element(By.XPATH, self.price_in_cart_full)
        value_price_in_cart_full_filled = value_price_in_cart_full.text
        return value_price_in_cart_full_filled

    def get_text_under_quantity(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.text_under_quantity)))
        return self.driver.find_element(By.XPATH, self.text_under_quantity)

    def get_text_under_sum(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.text_under_sum)))
        return self.driver.find_element(By.XPATH, self.text_under_sum)

    def get_agreement_in_cart(self):
        # return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.agreement_in_cart)))
        return self.driver.find_element(By.XPATH, self.agreement_in_cart)

    def get_basket_icon(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.basket_icon)))
        return self.driver.find_element(By.XPATH, self.basket_icon)

    def get_favourites_option(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.favourites_option)))
        return self.driver.find_element(By.XPATH, self.favourites_option)

    def get_delivery_title(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.delivery_title)))
        dt = self.driver.find_element(By.XPATH, self.delivery_title)
        dt_value = dt.text
        print('Идентифицирован раздел: ', dt_value)
        return dt_value

    def get_payment_methods(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.payment_methods)))
        pm = self.driver.find_element(By.XPATH, self.payment_methods)
        pm_value = pm.text
        print('Идентифицирован раздел: ', pm_value)
        return pm_value

    def get_cart_icon(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.cart_icon)))
        return self.driver.find_element(By.XPATH, self.cart_icon)

    def get_empty_cart_text(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.empty_cart_text)))
        return self.driver.find_element(By.XPATH, self.empty_cart_text)


# Actions - здесь создаются методы непосредственного взаимодействия с элементами главной страницы

    def click_place_order_button(self):
        self.get_place_order_button().click()
        print('Кнопка "Оформить заказ" нажата')

    def click_item_title_in_cart(self):
        self.get_item_title_in_cart().click()
        print('Клик на название товара в корзине сделан')

    def click_plus_button(self):
        self.get_plus_button().click()
        print('Кнопка увеличения количества товара (+) нажата')

    def click_minus_button(self):
        self.get_minus_button().click()
        print('Кнопка уменьшения количества товара (-) нажата')

    def click_agreement_in_cart(self):
        self.get_agreement_in_cart().click()
        print('Согласие с ожиданием товара подтверждено / отменено')

    def click_basket_icon(self):
        self.get_basket_icon().click()
        print('Клик на иконку корзины сделан (удаление товара)')

    def click_favourites_option(self):
        self.get_favourites_option().click()
        print('Опция "Добавить в избранное" активирована / деактивирована"')

    def click_cart_icon(self):
        self.get_cart_icon().click()
        print('Иконка корзины вверху экрана нажата')

    def driver_basic(self):

        self.driver.get(self.url)
        self.driver.maximize_window()


# Scenario - здесь реализуется сценарий взаимодействия с главной страницей

    def place_order(self):
        Logger.add_start_step(method='place_order')
        time.sleep(1)
        self.assert_word(self.get_item_title_in_cart(), 'Краска акриловая "VISTA-ARTISTA" idea декоративная глянцевая IGA-50 50 мл 102 Белая (White)')
        assert self.get_price_in_cart_1() == 130
        print('Совпадение по цене найдено')
        self.click_plus_button()
        assert self.get_price_in_cart_1() == 260
        print('Совпадение по цене найдено')
        self.get_text_under_quantity()
        print('Найден скрытый текст #1 (доступен только после увеличения объёма заказа)')
        self.get_text_under_sum()
        print('Найден скрытый текст #2 (доступен только после увеличения объёма заказа)')
        self.get_agreement_in_cart()
        print('Найден скрытый текст #3 (доступен только после увеличения объёма заказа)')
        self.click_minus_button()
        assert self.get_price_in_cart_1() == 130
        print('Совпадение по цене найдено')
        time.sleep(1)
        self.click_place_order_button()
        assert self.get_payment_methods() == 'СПОСОБ ОПЛАТЫ'
        print('Форма оплаты верифицирована (по наличию раздела: СПОСОБ ОПЛАТЫ)')
        assert self.get_delivery_title() == 'ДОСТАВКА'
        print('Форма оплаты верифицирована (по наличию раздела: ДОСТАВКА)')
        Logger.add_end_step(url=self.driver.current_url, method='place_order')

    def throw_item_from_cart(self):
        Logger.add_start_step(method='throw_item_from_cart')
        time.sleep(1)
        self.click_basket_icon()
        time.sleep(1)
        self.click_cart_icon()
        assert self.get_empty_cart_text().text == 'В ВАШЕЙ КОРЗИНЕ ПОКА НИЧЕГО НЕТ'
        print('Корзина пуста - проверено')
        Logger.add_end_step(url=self.driver.current_url, method='throw_item_from_cart')


    # python -m pytest -s -v