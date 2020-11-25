import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                 help="Choose from languages: en, ru, etc.")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
        chrome_opt = webdriver.ChromeOptions()
        # удаляем gpu ошибку из терминала
        chrome_opt.add_argument('--disable-gpu')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        # path to driver
        path = r"C:/chromedriver/chromedriver.exe"
        # declare and initialize driver variable
        browser = webdriver.Chrome(executable_path=path, options=options, chrome_options=chrome_opt)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()