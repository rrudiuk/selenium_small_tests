import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_presence(browser):
    browser.get(link)
    add_to_card_btn = browser.find_element_by_css_selector("button.btn-add-to-basket")
    time.sleep(5)
    assert add_to_card_btn is not None, 'Кнопка добавления товара в корзину не найдена!'
    # assert button.is_enabled()
    # assert EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    #assert len(
        # add_to_card_btn) > 0, 'Кнопка добавления товара в корзину не найдена!'  # Проверка наличия кнопки на странице
