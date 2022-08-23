import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

'''Создание класса Profile Page, дочернего по отношению к Base'''

class Profile_page(Base):

    url = 'https://leonardo.ru/profile/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators - здесь хранятся локаторы для работы с главной страницей

    # BASIC
    edit_option = '//a[@href="/profile/edit/"]'
    my_profile = '/html/body/div[2]/div[3]/div[1]/div/div/div[2]/ul/li[1]/a'
    profile_name = '//*[@id="order_form"]/div[1]/div/div[1]/div[1]/input'
    profile_surname = '//*[@id="order_form"]/div[1]/div/div[2]/div[1]/div[2]/input'
    profile_phone = '//*[@id="order_form"]/div[1]/div/div[1]/div[2]/input'
    save_changes = '//*[@id="order_form"]/div[2]/div/div[3]/div[2]/input'

    # CHECK SAVINGS
    saving_marker = '/html/body/div[2]/div[3]/div[2]/div/div/div[2]' #слово "Сохранено!" после нажатия кнопки
    name_marker = '/html/body/div[2]/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/span'

# Getters - здесь создаются методы получения доступа к нужным кнопкам главной страницы

    def get_edit_option(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.edit_option)))
        #return self.driver.find_element(By.XPATH, self.edit_option)

    def get_my_profile(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.my_profile)))
        #return self.driver.find_element(By.XPATH, self.my_profile)

    def get_profile_name(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.profile_name)))
        #return self.driver.find_element(By.XPATH, self.profile_name)

    def get_profile_surname(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.profile_surname)))
        #return self.driver.find_element(By.XPATH, self.profile_surname)

    def get_profile_phone(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.profile_phone)))
        #return self.driver.find_element(By.XPATH, self.profile_phone)

    def get_save_changes(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.save_changes)))
        #return self.driver.find_element(By.XPATH, self.save_changes)

    def get_saving_marker(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.saving_marker)))
        #return self.driver.find_element(By.XPATH, self.saving_marker)

    def get_name_marker(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.name_marker)))
        #return self.driver.find_element(By.XPATH, self.name_marker)



# Actions - здесь создаются методы непосредственного взаимодействия с элементами главной страницы

    def click_edit_option(self):
        self.get_edit_option().click()
        print('Клик по разделу "Редактировать профиль" сделан')
        self.assert_url('https://leonardo.ru/profile/edit/')

    def click_my_profile(self):
        self.get_my_profile().click()
        print('Клик по разделу "Мой профиль" сделан')
        self.assert_url('https://leonardo.ru/profile/')

    def input_profile_name(self):
        self.get_profile_name().clear()
        self.get_profile_name().send_keys('Арнольд Иванович')
        print('Поле имени заполнено')

    def input_profile_surname(self):
        self.get_profile_surname().clear()
        self.get_profile_surname().send_keys('Шварценеггер')
        print('Поле фамилии заполнено')

    def input_profile_phone(self):
        self.get_profile_phone().clear()
        self.get_profile_phone().send_keys('123-456-789')
        print('Поле телефона заполнено')

    def click_save_changes(self):
        self.get_save_changes().click()
        print('Кнопка сохранения изменений нажата')
        self.assert_url('https://leonardo.ru/profile/edit/')

    def driver_basic(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

# Scenario - здесь реализуется сценарий взаимодействия с главной страницей

    def editing_profile(self):
        self.driver_basic()

        time.sleep(1.5)
        self.click_edit_option()

        time.sleep(1.5)
        self.input_profile_name()

        time.sleep(1.5)
        self.input_profile_surname()

        time.sleep(1.5)
        self.input_profile_phone()

        time.sleep(1.5)
        self.click_save_changes()

        time.sleep(1.5)
        self.assert_word(self.get_saving_marker(), 'Сохранено!')

        time.sleep(1.5)
        self.click_my_profile()

        time.sleep(1.5)
        self.assert_word(self.get_name_marker(), 'Арнольд Иванович')

        self.get_screenshot()


# python -m pytest -s -v
