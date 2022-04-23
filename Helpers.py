from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class YandexElements:
    LOCATOR_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup_visible")
    LOCATOR_LINKS = (By.CSS_SELECTOR, ".path .link")
    LOCATOR_NECESSARY_LINK = "tensor.ru"
    LOCATOR_IMAGES_LINK = (By.CLASS_NAME, "services-new__icon_images")
    LOCATOR_FIRST_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0")
    LOCATOR_NAME_FIRST_CATEGORY = "data-grid-text"
    LOCATOR_SEARCH_NAME = (By.CLASS_NAME, "input__control")
    LOCATOR_FIRST_IMG = (By.CLASS_NAME, "serp-item__link")
    LOCATOR_CHECK_FIRST_IMG = (By.CLASS_NAME, "ImagesViewer-Container")
    LOCATOR_ATRIBUTE_FIRST_IMG = (By.CLASS_NAME, "MMImage-Origin")
    LOCATOR_NEXT_IMAGE = (By.CLASS_NAME, "MediaViewer-ButtonNext")
    LOCATOR_ATRIBUTE_SECOND_IMAGE = (By.CLASS_NAME, "MMImage-Origin")
    LOCATOR_PREV_IMAGE = (By.CLASS_NAME, "MediaViewer-ButtonPrev")


class Helpers:

    def __init__(self):
        self.driver = webdriver.Chrome(r"chromedriver.exe")

    @staticmethod
    def check_find_link(searching_results, link):
        """
        Проверяем наличие нужной ссылки в результате поиска
        :param searching_results: список найденных ссылок
        :param link: ссылка которую нужно найти в списке
        """
        flag = False
        for index, i in enumerate(searching_results):
            if index > 4:
                break
            if link in i.text:
                flag = True
                break
        TestCase().assertTrue(flag, f"Не найдена ссылка на {link}")

    def find_element(self, locator):
        """
        Ищем нужный элемент на странице
        :param locator: локатор элемента
        :return: элемент найденный на странице
        """
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator), "Не дождались появления элемента")

    def find_elements(self, locator):
        """
        Ищем нужные элементы на странице
        :param locator: селектор элемента
        :return: элементы найденные на странице
        """
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(locator), "Не дождались появления элементов")

    def switch_windows(self, window):
        """
        Переключаемся на нужную вкладку браузера
        :param window: номер нужной вкладки
        :return: переключение на нужную вкладку
        """
        return self.driver.switch_to.window(self.driver.window_handles[window])

    def wait_open(self, locator, error="Элемент не найден"):
        """
        Проверяем, что на странице появился нужный элемент
        :param locator: селектор элемента
        :param error: Текст, который будет напечатан в случае ошибки
        """
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(locator), error)

    def find_search_text(self):
        """
        Получаем значение атрибута класса
        :return: Возвращаем текст из найденного атрибута
        """
        search_elem = self.find_element(YandexElements().LOCATOR_SEARCH_NAME)
        text = search_elem.get_attribute("value")
        return text
