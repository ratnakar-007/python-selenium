import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilis.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_home_page(self, get_data):
        log = self.get_logger()
        home_page = HomePage(self.dr)
        log.info("Entering Name: ")
        home_page.get_name_field().send_keys(get_data["name"])
        log.info("Entering Name: ")
        home_page.get_email_field().send_keys(get_data["email"])
        log.info("Entering Name: ")
        home_page.get_password_field().send_keys("9971969010")
        home_page.get_checkbox_field().click()
        self.select_option_by_text(home_page.get_gender_field(), get_data["gender"])
        home_page.get_employment_status_field().click()
        home_page.get_submit_field().click()
        message = home_page.get_success_message_field().text
        log.info("Success message is "+message)
        assert "success" in message
        self.dr.refresh()

    # # with tuples as parameter
    # @pytest.fixture(params=[("Chandler", "Bing", "Male"), ("Monica", "Geller", "Female")])
    # def get_data(self, request):
    #     return request.param

    # with dictonary as parameter
    @pytest.fixture(params=HomePageData.home_page_test_data("Testcase2"))
    def get_data(self, request):
        return request.param
