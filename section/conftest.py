import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	parser.addoption('--language', action='store', default="en",
                 help="Choose from languages: en, ru, etc.")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # path to driver
    path = r"C:/chromedriver/chromedriver.exe"
    # declare and initialize driver variable
    browser = webdriver.Chrome(executable_path=path, options=options)
    yield browser

    print("\nquit browser..")
    browser.quit()