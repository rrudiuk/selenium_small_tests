from selenium import webdriver
import time

link = "http://google.com"

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

    browser.execute_script("document.title='Script executing';alert('Robots at work');")


    # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()