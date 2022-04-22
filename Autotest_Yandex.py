from selenium.webdriver.common.keys import Keys
import unittest
from Helpers import Helpers, YandexElements


class TestUI(unittest.TestCase):

    def setUp(self):
        self.helpers = Helpers()
        self.ya_elem = YandexElements()
        self.driver = self.helpers.driver
        self.driver.get("https://yandex.ru/")
        self.driver.maximize_window()

    def test_1(self):
        search = 'Тензор'

        # Нашли поле поиска
        search_field = self.helpers.find_element(self.ya_elem.LOCATOR_SEARCH_FIELD)

        # Вводим в поле поиска "Тензор"
        search_field.send_keys(search)

        # Проверяем, что появились варианты поиска
        self.helpers.wait_open(self.ya_elem.LOCATOR_SUGGEST)

        # Нажимаем ENTER, появляются результаты поиска
        search_field.send_keys(Keys.ENTER)

        # Проверяем наличие ссылки в результатах поиска
        searching_results = self.helpers.find_elements(self.ya_elem.LOCATOR_LINKS)

        # Ищем в результатах поиска нужную ссылку
        self.helpers.check_find_link(searching_results, self.ya_elem.LOCATOR_NECESSARY_LINK)

    def test_2(self):
        # открываем картинки
        self.helpers.find_element(self.ya_elem.LOCATOR_IMAGES_LINK).click()

        # Переключаемся на вторую вкладку
        self.helpers.switch_windows(1)

        # Получаем элемент первой категории
        category_elem = self.helpers.find_element(self.ya_elem.LOCATOR_FIRST_CATEGORY)

        # Из элемента первой категории получаем название категории
        category_name = category_elem.get_attribute(self.ya_elem.LOCATOR_NAME_FIRST_CATEGORY)

        # Кликаем на элемент первой категории
        category_elem.click()

        # Получаем текст из поля поиска
        search_name = self.helpers.find_search_text()

        # Проверяем совпадение названия категорий
        self.assertEqual(category_name, search_name, 'Названия категорий разные')

        # Открываем первую картинку
        self.helpers.find_elements(self.ya_elem.LOCATOR_FIRST_IMG)[0].click()

        # Проверяем, что первая картинка открылась
        self.helpers.wait_open(self.ya_elem.LOCATOR_CHECK_FIRST_IMG, 'Первая картинка не открылась')

        # Получаем атрибут первой картинки
        image_1 = self.helpers.find_element(self.ya_elem.LOCATOR_ATRIBUTE_FIRST_IMG).get_attribute('src')

        # Переключаемся на следущую картинку
        self.helpers.find_element(self.ya_elem.LOCATOR_NEXT_IMAGE).click()

        # Получаем атрибут второй картинки
        image_2 = self.helpers.find_element(self.ya_elem.LOCATOR_ATRIBUTE_SECOND_IMAGE).get_attribute('src')

        # Проверяем, что картинка изменилась после переключения
        self.assertNotEqual(image_1, image_2, "Картинка не изменилась")

        # Переключаемся на предыдущую картинку
        self.helpers.find_element(self.ya_elem.LOCATOR_PREV_IMAGE).click()

        # Еще раз получаем атрибут первой картинки
        image_1_prev = self.helpers.find_element(self.ya_elem.LOCATOR_ATRIBUTE_FIRST_IMG).get_attribute('src')

        # Проверяем, что первая картинка осталась та же самая после переключения вперед назад
        self.assertEqual(image_1, image_1_prev, "Картинки разные")

    def tearDown(self):
        # Закрывает драйвер
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
