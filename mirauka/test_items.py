import time


def test_guest_should_see_add_to_basket_button (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # time.sleep(30)
    add_to_basket_button = browser.find_element_by_css_selector(".btn.btn-add-to-basket")
    assert add_to_basket_button.is_displayed()
