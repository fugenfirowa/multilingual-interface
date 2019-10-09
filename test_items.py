link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_if_add_to_basket_button_exists(browser):
    browser.get(link)
    assert browser.find_element_by_class_name('btn-add-to-basket'),  "No Add to basket button found"