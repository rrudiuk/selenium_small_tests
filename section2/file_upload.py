from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try: 
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    chrome_opt = webdriver.ChromeOptions()
    # удаляем gpu ошибку из терминала
    chrome_opt.add_argument('--disable-gpu')
    # path to driver
    path = r"C:/chromedriver/chromedriver.exe"
    # declare and initialize driver variable
    browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_opt)
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Ruslan")
    browser.find_element_by_name("lastname").send_keys("Ruslan")
    browser.find_element_by_name("email").send_keys("example@example.com")

    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')        # добавляем к этому пути имя файла
    browser.find_element_by_id("file").send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()