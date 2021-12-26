import time

from .BasicPage import BasicPage
from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_WINDOW = (By.ID, 'text')
    SUGGEST_WINDOW = (By.XPATH, "//div[@class='mini-suggest__popup mini-suggest__popup_svg_yes mini-suggest__popup_theme_tile']")
    SEARCH_BUTTON = (By.XPATH, "//div[@class='search2__button']")
    RESULTS = (By.XPATH, "//div[@class='Path Organic-Path path organic__path']/a")


class SearchPage(BasicPage):
    """ step 2 убедиться в наличии поля поиска """
    def find_search_window(self):
        search_window = self.find_element(SearchPageLocators.SEARCH_WINDOW)
        return  search_window
    """ step 3 ввести слово в окно поиска """
    def enter_word(self, word):
        search_field = self.find_element(SearchPageLocators.SEARCH_WINDOW)
        search_field.click()
        for i in word:
            time.sleep(1)
            search_field.send_keys(i)
        return search_field

    """ step 4 проверить таблицу с подсказками """
    def wait_suggest(self):
        pass

    """ step 3^"""
    def click_on_the_search_button(self):
        return self.find_element(SearchPageLocators.SEARCH_BUTTON,time=2).click()

    """ step 5 check results """
    def check_navigation_bar(self):
        all_links = self.find_elements(SearchPageLocators.RESULTS,time=2)
        links = self.get_links_name(all_links)
        clear_links = self.check_link(links)
        return clear_links