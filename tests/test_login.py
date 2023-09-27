import time
from pageObjects.LoginPage import LoginPage

import pytest as pytest


# class TestLogin:
    # @pytest.mark.login
    # @pytest.mark.positive
    # @pytest.mark.parametrize("username, password", [("p8admin", "V3ga123456")])
   #  def test_login_positive(self, driver, username, password):
        #l oginpage = LoginPage(driver)
        # loginpage.open_url()
       #  loginpage.execute_login(username, password)

        # assert loginpage.is_logout_button_displayed(), "Logout button should be visible"

    # @pytest.mark.login
    # @pytest.mark.negative
    # @pytest.mark.parametrize("username, password, expected_error_message",
                           #  [("incorrectUser", "V3ga123456",
                            #   "Your name or password is invalid. Please try again.\nClick here for details."),
                           #   ("p8admin", "incorrectPassword",
                           #    "Your name or password is invalid. Please try again.\nClick here for details.")])
   # def test_login_negative(self, driver, username, password, expected_error_message):
      #  login_page = LoginPage(driver)
     #   login_page.open_url()
      #  login_page.execute_login(username, password)
      #  assert login_page.get_error_message() == expected_error_message, "Error message is not expected"
