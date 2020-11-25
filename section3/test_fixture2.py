import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    chrome_opt = webdriver.ChromeOptions()
    # удаляем gpu ошибку из терминала
    chrome_opt.add_argument('--disable-gpu')
    # path to driver
    path = r"C:/chromedriver/chromedriver.exe"
    # declare and initialize driver variable
    browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_opt)

    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")