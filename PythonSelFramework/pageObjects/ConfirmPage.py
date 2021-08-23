from selenium.webdriver.common.by import By


class confirmPage:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element_by_css_selector("input[class*='filter-input']").send_keys("ind")
    Location = (By.CSS_SELECTOR, "input[class*='filter-input']")

    # self.driver.find_element_by_xpath("//a[text()='India']").click()
    selectcountry = (By.XPATH, "//a[text()='India']")

    # self.driver.find_element_by_xpath("//label[@for='checkbox2']").click()
    terms = (By.XPATH, "//label[@for='checkbox2']")

    #self.driver.find_element_by_xpath("//input[contains(@class,'btn-success')]").click()
    purchase = (By.XPATH, "//input[contains(@class,'btn-success')]")

    # successText = self.driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text
    success = (By.XPATH, "//div[contains(@class,'alert-success')]")

    def typelocation(self):
        return self.driver.find_element(*confirmPage.Location)

    def selectIndia(self):
        return self.driver.find_element(*confirmPage.selectcountry)

    def agreeTerms(self):
        return self.driver.find_element(*confirmPage.terms)

    def purchaseItem(self):
        return self.driver.find_element(*confirmPage.purchase)

    def successText(self):
        return self.driver.find_element(*confirmPage.success)


