from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

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

    # Считываем значение Х
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id('answer').send_keys(y);

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radio_button = browser.find_element_by_css_selector("[for='robotsRule']")
    radio_button.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()