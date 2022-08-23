
from selenium.webdriver.common.by import By

from base.base_class import Base

'''Создание класса Main Page, дочернего по отношению к Base'''

class Knitting_page(Base):

    url = 'https://leonardo.ru/ishop/tree_1444732062/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators - здесь хранятся локаторы для работы с главной страницей

    link_caskets = '/html/body/div[2]/div/div[3]/div[2]/a'

# Getters - здесь создаются методы получения доступа к нужным кнопкам главной страницы

    def get_link_caskets(self):
        #return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_caskets))
        return self.driver.find_element(By.XPATH, self.link_caskets)

# Actions - здесь создаются методы непосредственного взаимодействия с элементами главной страницы

    def click_link_caskets(self):
        self.get_link_caskets().click()
        print('Клик по ссылке раздела шкатулок сделан')
        self.assert_url('https://leonardo.ru/ishop/tree_9538924894/')
        self.get_current_url()

# Scenario - здесь реализуется сценарий взаимодействия с главной страницей

    def scenario_knitting(self):
        self.get_current_url()
        self.click_link_caskets()




    # python -m pytest -s -v
