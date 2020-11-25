from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
        chrome_opt = webdriver.ChromeOptions()
        # удаляем gpu ошибку из терминала
        chrome_opt.add_argument('--disable-gpu')
        # path to driver
        path = r"C:/chromedriver/chromedriver.exe"
        # declare and initialize driver variable
        self.browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_opt)

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test..")
        # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
        chrome_opt = webdriver.ChromeOptions()
        # удаляем gpu ошибку из терминала
        chrome_opt.add_argument('--disable-gpu')
        # path to driver
        path = r"C:/chromedriver/chromedriver.exe"
        # declare and initialize driver variable
        self.browser = webdriver.Chrome(executable_path=path,chrome_options=chrome_opt)

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")