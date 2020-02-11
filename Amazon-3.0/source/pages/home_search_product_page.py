'''
@author: Divya
@email:deepuravishancar@gmail.com
@date:9th Jan
'''

from source.utilities.generic_methods import GenericMethods
import logging
import time
from source.utilities import custom_logger as cl


class Homepage_search_product(GenericMethods):
    """
    Searching products in Amazon
    """
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        # constructor chaining
        super().__init__(driver)
        self.driver = driver
        self.search_product_id = "twotabsearchtextbox"



    def searchBox(self, productName):
        # using self keyword we can access the methods in generic methods
        self.sendKeys(productName, self.search_product_id)
        self.elementClick("//input[@value='Go']","xpath")


    def clickOnProduct(self):
        self.elementClick("//span[text()='Apple iPhone XR (64GB) - Yellow']","xpath")



