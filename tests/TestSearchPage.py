from pages.SearchPage import SearchPage


def test_full_search(browser):
    search_page = SearchPage(browser)
    search_page.go_to_site()
    search_page.find_search_window().is_displayed()
    search_page.enter_word("Тензор")
    search_page.click_on_the_search_button()

def test_check_search_window(browser):
    search_page = SearchPage(browser)
    search_page.go_to_site()
    assert search_page.find_search_window().is_displayed()

def test_check_tensor_in_links(browser):
    search_page = SearchPage(browser)
    search_page.go_to_site()
    search_page.enter_word("Тензор")
    search_page.click_on_the_search_button()
    elements = search_page.check_navigation_bar()
    assert "tensor.ru" in elements
