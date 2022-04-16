from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn


@library
class Shop:

    def __init__(self):
        self.selLib = BuiltIn().get_library_instance("Selenium Library")

    # method name will be converted to keyword name Hello World
    @keyword
    def hello_world(self):
        print("Hello World")

    @keyword
    def add_items_to_cart_and_checkout(self, productsList):
        i = 1
        prodTitles = self.selLib.get_webelements("css:.card-title")

        for prod in prodTitles:
            if prod.text in productsList:
                self.selLib.click_button("(//div[@class='card-footer'])["+str(i)+"]/button")
            i = i + 1