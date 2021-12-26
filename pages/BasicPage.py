import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse

class BasicPage:
    """ базовый класс """
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/"

    def wait_click(self,locator,time=10):
        """ ожидает пока елемент не будет доступен для клика """
        return WebDriverWait(self.driver,time).until(EC.element_to_be_clickable(locator))

    def find_element(self, locator,time=10):
        """ поиск элемента """
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        """ поиск элементов """
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
    def go_to_site(self):
        """ переход на страницу """
        return self.driver.get(self.base_url)

    def get_links_name(self,webElement):
        """ извлекает атрибут href из собранных элементов"""
        links_list = []
        for i in webElement:
            links_list.append(i.get_attribute('href'))
        return links_list

    def check_link(self, links):
        """ принимает коллекцию ссылок, оставляет только домен    """
        result = [urlparse(u).netloc for u in links]
        return result

