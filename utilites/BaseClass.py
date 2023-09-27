import inspect

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
import logging


class BaseClass:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        # Создайте Logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Создайте обработчик для записи данных в файл
        logger_handler = logging.FileHandler('python_logging.log')
        logger_handler.setLevel(logging.INFO)

        # Создайте Formatter для форматирования сообщений в логе
        logger_formatter = logging.Formatter('%(asctime)s %(name)s - %(levelname)s - %(message)s')

        # Добавьте Formatter в обработчик
        logger_handler.setFormatter(logger_formatter)

        # Добавьте обработчик в Logger
        self.logger.addHandler(logger_handler)
        self.logger.info('Настройка логгирования окончена!')

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _find_elements(self, locator: tuple) -> WebElement:
        return self._driver.find_elements(*locator)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _is_displayed(self, locator: tuple) -> bool:
        return self._find(locator).is_displayed()

    def _open_url(self, url: str):
        self._driver.get(url)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _select_by_value(self, locator: tuple, value: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    def _get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger



