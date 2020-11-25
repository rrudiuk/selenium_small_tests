from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
chrome_opt = webdriver.ChromeOptions()
# удаляем gpu ошибку из терминала
chrome_opt.add_argument('--disable-gpu')
# path to driver
path = r"C:/chromedriver/chromedriver.exe"
# declare and initialize driver variable
browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_opt)
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text