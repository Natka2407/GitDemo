from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from utilites.BaseClass import BaseClass


class SearchDocuments(BaseClass):
    __search_button = (By.XPATH, "//span[text()='Search']")
    __confirm_window = (By.XPATH, "//div[text()='Confirm']")
    __ok_button = (By.XPATH, "//span[text()='OK']")
    __limit_result_message = (By.XPATH,
                              "//div[text()='Search result size exceeds the maximum allowable search results size of 5000 documents. Only the first 5000 results of your search will be displayed.']")
    __total_limit = (By.XPATH, "//label[text()='5000']")
    __total_documents = (By.XPATH,
                         "//label[@id='search-templates-vignette-tab-ext-162-documents_vg_extjs_document_Search_vignette-bbar-total_label2']")
    __title_field = (By.XPATH, "//input[@name='c_0']")
    __class_field = (By.XPATH, "//input[@name='c_3']")
    __class_field_text = (By.XPATH, "//ul[@class='x-list-plain']//li[text()='QA2']")
    __ssn_field = (By.XPATH, "//input[@name='c_4']")
    __start_modify_date_field = (By.XPATH, "//input[@name='ext-470_start-inputEl']")
    __end_modify_date_field = (By.XPATH, "//input[@name='ext-470_end-inputEl']")
    __modify_date_field = (By.XPATH, "//input[@name='ext-470_start-inputEl']")

    __class_value = (By.XPATH, "*[contains(text(),'QA2')]")
    __class_picker = (By.ID, "ext-465-trigger-picker")
    __start_date_picker = (By.ID, "ext-470_start-trigger-picker")
    __end_date_picker = (By.ID, "ext-470_end-trigger-picker")
    __modify_start_date_picker = (By.ID, "ext-470_start-picker-eventEl")
    __modify_end_date_picker = (By.ID, "ext-470_end-picker-eventEl")

    __modify_start_date_picker = (By.XPATH, "//table[@id='ext-470_start-picker-eventEl']")
    __date_selected = (By.CLASS_NAME, "x-datepicker-active x-datepicker-cell x-datepicker-selected")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def click_search(self):
        super()._click(self.__search_button)

    def is_results_limit_window_displayed(self) -> bool:
        super()._wait_until_element_is_visible(self.__confirm_window)
        if super()._is_displayed(self.__confirm_window):
            return True
        else:
            return False

    def click_ok_on_confirm_window(self):
        super()._click(self.__ok_button)

    def get_limit_result__message(self) -> str:
        return super()._get_text(self.__limit_result_message, time=3)

    def get_total_documents(self) -> str:
        return super()._get_text(self.__total_documents, time=3)

    def search_by_title(self, doc_title: str):
        # self.logger.warning('start search_by_title!')
        super()._type(self.__title_field, doc_title)
        super()._click(self.__search_button)
        # self.logger.warning('end search_by_title!')

    def search_by_title_and_ssn(self, doc_title: str, ssn: str):
        super()._type(self.__title_field, doc_title)
        super()._type(self.__ssn_field, ssn)
        super()._click(self.__search_button)

    def form_xpath(self, class_value: str):
        class_xpath = (By.XPATH, "//li[text()='" + class_value + "']")
        return class_xpath

    def search_by_class(self, class_value: str):
        super()._click(self.__class_picker)
        super()._click(self.form_xpath(class_value))
        super()._click(self.__search_button)

    def search_by_modified_date(self, date_value: str):
        super()._click(self.__start_date_picker)
        super()._type(self.__start_modify_date_field, date_value)
        super()._click(self.__search_button)

    def search_by_modified_date_and_class(self, date_value: str, class_value: str):
        super()._click(self.__class_picker)
        super()._click(self.form_xpath(class_value))
        super()._click(self.__start_date_picker)
        super()._type(self.__start_modify_date_field, date_value)
        super()._click(self.__search_button)

    def search_by_modified_date_range(self, start_date_value: str, end_date_value: str):
        super()._click(self.__start_modify_date_field)
        super()._type(self.__start_modify_date_field, start_date_value)
        super()._click(self.__end_modify_date_field)
        super()._type(self.__end_modify_date_field, end_date_value)
        super()._click(self.__search_button)
