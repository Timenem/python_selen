import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from .BasicPage import BasicPage


class ImagePageLocators:
    """ используемые локаторы """
    IMAGES_LINK = (By.PARTIAL_LINK_TEXT, "Картинки")
    FIRST_CATEGORY_IMAGES = (By.XPATH, "//div[@class='PopularRequestList-SearchText']")
    FIRST_IMAGE_FROM_ALL_IMAGES = (By.CLASS_NAME, 'serp-item__link')
    SEARCH_WINDOW_QUERY = (By.CSS_SELECTOR, ".input__control")
    IMAGE_CONTAINER = (By.CLASS_NAME, 'MMImageContainer')

    IMAGE_CONTAINER_NAME = (By.CSS_SELECTOR, ".MMImage-Preview")
    NEXT_BTN = (By.XPATH,
                "//div[@class='CircleButton CircleButton_type_next CircleButton_type MediaViewer-Button MediaViewer-Button_hovered MediaViewer_theme_fiji-Button MediaViewer-ButtonNext MediaViewer_theme_fiji-ButtonNext']")

    PREV_BTN = (By.XPATH,
                "//div[@class='CircleButton CircleButton_type_prev CircleButton_type MediaViewer-Button MediaViewer-Button_hovered MediaViewer_theme_fiji-Button MediaViewer-ButtonPrev MediaViewer_theme_fiji-ButtonPrev']")


class ImagePage(BasicPage):
    def find_image_by_link(self):
        self.find_element(ImagePageLocators.IMAGES_LINK).click()
        window = self.driver.switch_to.window(self.driver.window_handles[1])
        return window

    def get_first_category_name(self):
        """
        ищет первую категорию из представленных на странице,возвращает название категории
        """
        return self.find_element(ImagePageLocators.FIRST_CATEGORY_IMAGES).get_attribute('textContent')

    def get_url(self):

        return self.driver.current_url

    def open_first_category_image(self):
        """ открывает первую категорию """
        return self.find_element(ImagePageLocators.FIRST_CATEGORY_IMAGES).click()

    def page_refresh(self):
        """ перезагружает страницу для получения value  в методе get_image_name_from_search_window"""
        self.driver.refresh()

    def get_image_name_from_search_window(self):
        """ находит поле ввода запроса и возвращет  запрос  """
        return self.find_element(ImagePageLocators.SEARCH_WINDOW_QUERY).get_attribute('value')

    def open_first_image(self):
        """ открывет первое изображение из представленных на странице """
        all_images = self.find_elements(ImagePageLocators.FIRST_IMAGE_FROM_ALL_IMAGES)
        return all_images[0].click()

    def image_options(self):
        """ поиск контейнера изображения """
        return self.find_element(ImagePageLocators.IMAGE_CONTAINER)

    def get_image_uri(self):
        """ извлекает путь картинки из контейнера для сравнения """
        return self.find_element(ImagePageLocators.IMAGE_CONTAINER_NAME).get_attribute("src")

    def press_to_image_btn(self):
        """ выполняет нажатие на кнопки next """
        action = ActionChains(self.driver)
        action.move_to_element(self.wait_click(ImagePageLocators.IMAGE_CONTAINER)).perform()
        time.sleep(2)
        self.find_element(ImagePageLocators.NEXT_BTN).click()
        time.sleep(2)
        action.move_to_element(self.wait_click(ImagePageLocators.IMAGE_CONTAINER)).perform()
