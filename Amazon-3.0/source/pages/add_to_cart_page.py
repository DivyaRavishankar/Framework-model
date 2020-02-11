'''
@author: Divya
@email:deepuravishancar@gmail.com
@date:9th Jan
'''
from source.pages.home_search_product_page import Homepage_search_product
from source.utilities.generic_methods import GenericMethods
import logging
from source.utilities.excel import *
import time
from source.utilities import custom_logger as cl


class Homepage_add_product(GenericMethods):
    """
    Searching products in Amazon
    """
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        # constructor chaining
        super().__init__(driver)
        self.driver = driver
        Homepage_search_product(driver)

    def add_product_cart(self):
        self.switch_to_child_window(self.driver)
        self.timesleep(6)
        self.elementClick("//input[@id='add-to-cart-button']","xpath")


    def verification(self):
        self.elementClick("//a[@id='hlb-view-cart-announce']", "xpath")
        exp_result=get_value("Cart","TC_002","SuccessMessage")
        act_result=self.gettext("(//span[contains(text(),'Apple iPhone XR (64GB) - Yellow')])[1]", "xpath")
        assert exp_result == act_result,"False"
        self.log.info("Verification done->pass")


