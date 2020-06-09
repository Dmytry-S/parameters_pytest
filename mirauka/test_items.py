from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_presence_of_buy_button(browser):
    browser.get(link)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
    )
    assert browser.find_element_by_css_selector(".btn-add-to-basket").is_displayed()
