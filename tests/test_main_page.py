from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    # link = "http://selenium1py.pythonanywhere.com/"
    # browser.get(link)
    # login_link = browser.find_element_by_css_selector("#login_link")
    # login_link.click()
