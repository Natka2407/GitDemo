import time

import pytest as pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchDocuments import SearchDocuments


# @pytest.mark.usefixtures("driver")

class TestSearch:

    @pytest.mark.search
    @pytest.mark.parametrize("username, password", [("p8admin", "V3ga123456")])
    def test_search_all(self, driver, username, password):

        expected_limit_message = "Search result size exceeds the maximum allowable search results size of 5000 documents. Only the first 5000 results of your search will be displayed."

        loginpage = LoginPage(driver)
        loginpage.open_url()
        loginpage.execute_login(username, password)

        searchpage = SearchDocuments(driver)
        searchpage.click_search()

        if searchpage.is_results_limit_window_displayed():
            assert searchpage.get_limit_result__message() == expected_limit_message, "Limit message is not expected"
            searchpage.click_ok_on_confirm_window()
        else:
            print("Confirm is not displayed")

    @pytest.mark.search
    @pytest.mark.parametrize("username, password, title_value, expected_limit_documents",
                             [("p8admin", "V3ga123456", "nktest", "4")])
    def test_search_by_title(self, driver, username, password, title_value, expected_limit_documents):
        loginpage = LoginPage(driver)
        loginpage.open_url()
        loginpage.execute_login(username, password)

        searchpage = SearchDocuments(driver)
        searchpage.search_by_title(title_value)

        assert searchpage.get_total_documents() == expected_limit_documents, "Limit documents is not expected"

    @pytest.mark.search
    @pytest.mark.parametrize("username, password, title_value, ssn_value, expected_limit_documents",
                             [("p8admin", "V3ga123456", "test1", "123", "2")])
    def test_search_by_title_and_ssn(self, driver, username, password, title_value, ssn_value,
                                     expected_limit_documents):
        loginpage = LoginPage(driver)
        loginpage.open_url()
        loginpage.execute_login(username, password)

        searchpage = SearchDocuments(driver)
        searchpage.search_by_title_and_ssn(title_value, ssn_value)

        assert searchpage.get_total_documents() == expected_limit_documents, "Limit documents is not expected"

    @pytest.mark.search
    @pytest.mark.parametrize("username, password, class_value, number_of_docs",
                             [("p8admin", "V3ga123456", "QA2", "799")])
    def test_search_by_class(self, driver, username, password, class_value, number_of_docs):
        loginpage = LoginPage(driver)
        loginpage.open_url()
        loginpage.execute_login(username, password)

        searchpage = SearchDocuments(driver)
        searchpage.search_by_class(class_value)
        assert searchpage.get_total_documents() == number_of_docs, "Limit documents is not expected"

    @pytest.mark.parametrize("username, password, date_value, number_of_docs",
                             [("p8admin", "V3ga123456", "06/01/2023", "17")])
    def test_search_by_modified_date(self, driver, username, password, date_value, number_of_docs):
        loginpage = LoginPage(driver)
        loginpage.open_url()
        loginpage.execute_login(username, password)

        searchpage = SearchDocuments(driver)
        searchpage.search_by_modified_date(date_value)
        assert searchpage.get_total_documents() == number_of_docs, "Limit documents is not expected"

    @pytest.mark.parametrize("username, password, date_value, class_value, number_of_docs",
                             [("p8admin", "V3ga123456", "06/01/2023", "QA2", "10")])
    def test_search_by_modified_date_and_class(self, driver, username, password, date_value, class_value,
                                               number_of_docs):
        loginpage = LoginPage(driver)
        loginpage.open_url()
        loginpage.execute_login(username, password)

        searchpage = SearchDocuments(driver)
        searchpage.search_by_modified_date_and_class(date_value, class_value)
        assert searchpage.get_total_documents() == number_of_docs, "Limit documents is not expected"

    @pytest.mark.parametrize("username, password, start_date_value,  end_date_value, number_of_docs",
                             [("p8admin", "V3ga123456", "06/01/2023", "06/06/2023", "1")])
    def test_search_by_modified_date_range(self, driver, username, password, start_date_value, end_date_value,
                                           number_of_docs):
        loginpage = LoginPage(driver)
        loginpage.open_url()
        loginpage.execute_login(username, password)

        searchpage = SearchDocuments(driver)
        searchpage.search_by_modified_date_range(start_date_value, end_date_value)
        assert searchpage.get_total_documents() == number_of_docs, "Limit documents is not expected"
