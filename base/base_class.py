import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    # Получаем текущий url сайта
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Текущий URL: ', get_url)

    # Проверяем, что попали на нужную страницу (по ключевому слову)

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Проверка по ключевому слову прошла успешно')

    # Проверяем, что попали на нужную страницу (по адресу страницы)

    def assert_url(self, result):
        value_url = self.driver.current_url
        assert value_url == result
        print('Проверка по адресу страницы прошла успешно')
        self.get_current_url()

    # Делаем скриншот страницы

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y-%m-%d__%H.%M.%S')
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\rdykin\\PycharmProjects\\BookStore\\screenshots\\' + name_screenshot)
        print('Скриншот сохранён')

