from source.pages.home_search_product_page import Homepage_search_product as searchprod
from source.pages.add_to_cart_page import Homepage_add_product as addprod
from source.utilities.webdriver_factory import WebDriverFactory

#to search the product in search box
class HomeSearchProduct(WebDriverFactory):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def searchProduct(self,name):
        searchprod(self.driver).searchBox(name)
        searchprod(self.driver).clickOnProduct()

    def addproduct(self):
        addprod(self.driver).add_product_cart()
        # addprod(self.driver).clickAddToCartBtn()
        addprod(self.driver).verification()


