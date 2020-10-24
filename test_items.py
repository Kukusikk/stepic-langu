import time 

def test_bucket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/ '
    browser.get(link)
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.find_element_by_xpath("//*[@id='add_to_basket_form']")

    assert True