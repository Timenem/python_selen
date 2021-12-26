import time

from pages.ImagePage import ImagePage


def test_full(browser):
    image_page = ImagePage(browser)
    image_page.go_to_site()
    time.sleep(2)
    image_page.find_image_by_link()
    cat_name = image_page.get_first_category_name()
    image_page.open_first_category_image()
    image_page.page_refresh()
    time.sleep(4)
    query_name = image_page.get_image_name_from_search_window()
    image_page.open_first_image()
    assert cat_name == query_name, "разные имена "
    time.sleep(2)
    image_cont = image_page.image_options()
    image_uri = image_page.get_image_uri()
    image_page.press_to_image_btn()
    assert image_cont.is_displayed()


def test_url(browser):
    image_page = ImagePage(browser)
    image_page.go_to_site()
    time.sleep(2)
    image_page.find_image_by_link()
    image_page.open_first_category_image()
