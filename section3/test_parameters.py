import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    chrome_opt = webdriver.ChromeOptions()
    # удаляем gpu ошибку из терминала
    chrome_opt.add_argument('--disable-gpu')
    # path to driver
    path = r"C:/chromedriver/chromedriver.exe"
    # declare and initialize driver variable
    browser = webdriver.Chrome(executable_path=path, options=chrome_opt)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", 
    "236898", "236899", "236903", "236904", "236905"])
def test_use_parameters(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)

    answer = math.log(int(time.time()))
    print(answer)

    time.sleep(7)

    text_input = browser.find_element_by_css_selector('textarea.textarea')
    text_input.clear()
    text_input.send_keys(str(answer))

    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    time.sleep(2)

    actual_result = browser.find_element_by_css_selector(".smart-hints__hint").text
    expected_result = "Correct!"

    assert actual_result == expected_result

# pytest -s -v test_parameters.py