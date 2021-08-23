from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import confirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    #   products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
    cards = (By.XPATH, "//div[@class='card h-100']/div/h4/a")

    # card.find_element_by_xpath("div[2]/button")
    addToCart = (By.XPATH, "//div[@class='card h-100']/div[2]/button")

    # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    # self.driver.find_element_by_css_selector("button[class*='btn-success']").click()
    finalcheckout = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def getCards(self):
        return self.driver.find_elements(*CheckOutPage.cards)

    def CartButton(self):
        return self.driver.find_elements(*CheckOutPage.addToCart)

    def CheckOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def finalCheckOutItems(self):
        self.driver.find_element(*CheckOutPage.finalcheckout).click()
        return confirmPage(self.driver)