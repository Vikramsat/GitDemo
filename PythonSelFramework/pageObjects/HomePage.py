from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage
import pytest


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
#    self.driver.find_element_by_css_selector("a[href*='shop']").click()

    # driver.find_element_by_css_selector("input[name = 'name']").send_keys("Vikram")
    name = (By.CSS_SELECTOR, "input[name = 'name']")

    # driver.find_element_by_name("email").send_keys("abc@google.co")
    email = (By.NAME, "email")

    # driver.find_element_by_id("exampleInputPassword1").send_keys("hello")
    pwd = (By.ID, "exampleInputPassword1")

    # driver.find_element_by_id("exampleCheck1").click()
    Icecrm = (By.ID, "exampleCheck1")

    # driver.find_element_by_xpath("//input[@type = 'submit']").click()
    submit = (By.XPATH, "//input[@type = 'submit']")

    success = (By.CLASS_NAME, "alert-success")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckOutPage(self.driver)

    def entername(self):
        return self.driver.find_element(*HomePage.name)

    def enteremail(self):
        return self.driver.find_element(*HomePage.email)

    def enterpwd(self):
        return self.driver.find_element(*HomePage.pwd)

    def checkicecream(self):
        return self.driver.find_element(*HomePage.Icecrm)

    def submitbutton(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessText(self):
        return self.driver.find_element(*HomePage.success)