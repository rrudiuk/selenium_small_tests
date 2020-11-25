import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class runTests(unittest.TestCase):
    # --- Pre - Condition ---
    def setUp(self):
        # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
        chrome_opt = webdriver.ChromeOptions()
        # удаляем gpu ошибку из терминала
        chrome_opt.add_argument('--disable-gpu')
        # path to driver
        path = r"C:/chromedriver/chromedriver.exe"
        # declare and initialize driver variable
        self.browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_opt)
        # browser should be loaded in maximized window
        self.browser.maximize_window()
        # driver should wait implicitly for a given duration, for the element under consideration to load.
        # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
        self.browser.implicitly_wait(10)  # 10 is in seconds


    def testFirstLink(self):
        link = "http://suninjuly.github.io/registration1.html"

        self.browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = self.browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input').send_keys("Ivan")
        input2 = self.browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input').send_keys("Petrov")
        input2 = self.browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input').send_keys("example@example.com")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        expected_result = "Congratulations! You have successfully registered!"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, expected_result)

    def testSecondLink(self):
        link = "http://suninjuly.github.io/registration2.html"

        self.browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = self.browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input').send_keys("Ivan")
        input2 = self.browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input').send_keys("Petrov")
        input2 = self.browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input').send_keys("example@example.com")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        expected_result = "Congratulations! You have successfully registered!"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, expected_result)


    # --- post - condition ---
    def tearDown(self):
        # to close the browser
        self.browser.quit()

if __name__ == "__main__":
    unittest.main() 