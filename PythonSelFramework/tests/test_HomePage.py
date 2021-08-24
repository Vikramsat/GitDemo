from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from utilities.BaseClass import Baseclass
from TestData.HomePageData import HomePageData
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestHomePage(Baseclass):

    def test_formSubmission(self, getData):
        print("Hi I am added by GitDemo1")
        print("Hi I am added by GitDemo2")
        log = self.getlogger()
        homepage = HomePage(self.driver)

        log.info("Firstname:"+getData["Firstname"])
        homepage.entername().send_keys(getData["Firstname"])
        homepage.enteremail().send_keys(getData["Email"])
        homepage.enterpwd().send_keys(getData["Password"])
        homepage.checkicecream().click()

        dropdown = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        dropdown.select_by_visible_text(getData["Gender"])

        homepage.submitbutton().click()

        assert "Success" in homepage.getSuccessText().text

        self.driver.refresh()

    def changesforBranch(self):
        print("Changes made in branch")

    @pytest.fixture(params=HomePageData.testData("Testcase2"))
    def getData(self, request):
        return request.param