from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import confirmPage
from utilities.BaseClass import Baseclass
from pageObjects.HomePage import HomePage

#@pytest.mark.usefixtures("setup")      #placed this fixture in BaseClass.py to make the code more optimized, and inheriting Baseclass in the below class
class TestOne(Baseclass):
    def test_e2e(self):

        log = self.getlogger()
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
#        self.driver.find_element_by_css_selector("a[href*='shop']").click()

#        checkOutPage = CheckOutPage(self.driver)   #Object creation done in shopItems() method
        confirmpage_obj = confirmPage(self.driver)  #creating object for confirmPage class
        log.info("Getting cards")
        cards = checkOutPage.getCards()
        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")


        print(cards)

        button = checkOutPage.CartButton()
        i = 0
        for i in range(len(cards)):
            if cards[i].text == 'Blackberry':
                log.info("Blackberry adding to cart")
                button[i].click()
                break
            i = i + 1

        # click on checkout
        log.info("Checking out items")
        #self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        checkOutPage.CheckOutItems().click()

        log.info("Final checkout")
        # click checkout on next page
        #self.driver.find_element_by_css_selector("button[class*='btn-success']").click()
        confirmpage_obj = checkOutPage.finalCheckOutItems()

        # Wait for page to load
        wait = WebDriverWait(self.driver, 8)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[class*='filter-input']")))

        log.info("Entering country as ind")
        # enter location india in next page
        # self.driver.find_element_by_css_selector("input[class*='filter-input']").send_keys("ind")
        confirmpage_obj.typelocation().send_keys("ind")

        #wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='India']")))
        self.verifyTextPresence("India")
        # self.driver.find_element_by_xpath("//a[text()='India']").click()
        confirmpage_obj.selectIndia().click()

        # click on agree terms
        #self.driver.find_element_by_xpath("//label[@for='checkbox2']").click()
        confirmpage_obj.agreeTerms().click()

        log.info("Purchasing item")
        # click on purchase
        # self.driver.find_element_by_xpath("//input[contains(@class,'btn-success')]").click()
        confirmpage_obj.purchaseItem().click()


        #successText = self.driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text
        successText = confirmpage_obj.successText().text
        log.info("Message: "+successText)
        assert 'Success! Thank you!' in successText

#        self.driver.get_screenshot_as_file("screen.png")

    # def test_sample(self):                    #Vikram's experiment
    #     self.driver.get("https://www.google.co.in/")