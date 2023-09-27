from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from utilites.BaseClass import BaseClass


class LoginPage(BaseClass):
    __url = "https://qa-appsrv-08c.intellective.com:9443/u7-vignette/main.jsp?theme=unity_next"
    __username_field = (By.ID, "user-nameext-33-inputEl")
    __password_field = (By.ID, "passwordext-33-inputEl")
    __submit_button = (By.ID, "button-1016-btnInnerEl")
    __logout_button_locator = (By.ID, "logoutbutton-ext-369")
    __error_message = (By.XPATH, "//*[contains(text(),'Your name or password is invalid. Please try again.')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_url(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_button)

    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message, time=3)

    def is_login_succesful(self) -> bool:
        try:
            # return self.driver.find_element(LoginPage.__logout_button)
            return super()._find(self.__logout_button_locator)
        except NoSuchElementException:
            return False

    def is_logout_button_displayed(self) -> bool:
        super()._wait_until_element_is_visible(self.__logout_button_locator)
        return super()._is_displayed(self.__logout_button_locator)



