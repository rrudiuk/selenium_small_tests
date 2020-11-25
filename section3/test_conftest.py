link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    add_to_card_btn = browser.find_element_by_css_selector("#login_link")