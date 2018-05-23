import unittest
from app.utils import create_driver_instance
from app.ui.home_page import HomePage
from app.ui.mobile_page import MobilePage
from app.ui.mobile_description_page_sonyxperia import MobileDescriptionPageSonyxperia
from selenium.webdriver.common.keys import Keys
import json


class Test_error_verification(unittest.TestCase):

    def setUp(self):
        self.browser = create_driver_instance.get_driver_instance()
        self.home_page = HomePage(self.browser)
        self.mobile_page = MobilePage(self.browser)
        self.mobile_description_page_sonyxperia = MobileDescriptionPageSonyxperia(self.browser)
        self.test_data = json.load(open("skynet-test/test/smoke/testdata.json",'r'))

    def tearDown(self):
        self.browser.close()

    def test_error_verification(self):

        #step 1 click on mobile menu
        self.home_page.get_mobile().click()
        #step2 click on add to cart of sony xperia
        self.mobile_page.get_add_to_cart_sonyxperia().click()
        #step3 update qty with 1000 and click on update
        self.mobile_description_page_sonyxperia.get_edit_sonyxperia().click()
        qty = self.mobile_description_page_sonyxperia.get_qty_sonyxperia()
        qty.send_keys(Keys.CONTROL,'a')
        qty.send_keys(self.test_data['qty'])
        self.mobile_description_page_sonyxperia.get_update_button().click()
        # step 5 verify error msg
        error_msg = self.mobile_description_page_sonyxperia.get_error_msg().text
        expected_error_msg_of_qty = self.test_data['expected_error_msg_of_qty']
        assert error_msg == expected_error_msg_of_qty
        '''# step 6 verify empty cart
        self.mobile_description_page_sonyxperia.get_empty_cart().click()
        empty_cart_msg = self.mobile_description_page_sonyxperia.get_empty_cart_msg()
        empty_cart_msg.text
        expected_empty_cart_msg = self.test_data['expected_empty_cart_msg']
        assert empty_cart_msg == expected_empty_cart_msg'''











        '''self.browser.find_element_by_xpath("//input[@type='text']/parent::td/ul[@class='cart-links']/li/a[contains(text(),'Edit')]").click()
        qty = self.browser.find_element_by_xpath("//div[@class='qty-wrapper']/input[@id='qty']")
        time.sleep(5)
        qty.send_keys(Keys.CONTROL,'a')
        qty.send_keys("1000")

        # step 4 click on update button
        self.browser.find_element_by_xpath("//div[@class='add-to-cart-buttons']/button/span/span[contains(text(),'Update Cart')]").click()

        # step 5 verify error msg

        actual_error_msg = self.browser.find_element_by_xpath("//ul[@class='messages']/li/ul/li/span[contains(text(),'The maximum quantity allowed for purchase is 500.')]").text
        expected_error_msg = 'The maximum quantity allowed for purchase is 500.'
        assert actual_error_msg == expected_error_msg

        # step 6 verify empty cart
        self.browser.find_element_by_xpath("//td[@class='a-right cart-footer-actions last']/button[@id='empty_cart_button']/span/span[contains(text(),'Empty Cart')]").click()
        actual_empty_cart_msg = self.browser.find_element_by_xpath("//h1[contains(text(),'Shopping Cart is Empty')]").text
        expected_empty_cart_msg = 'SHOPPING CART IS EMPTY'
        assert actual_empty_cart_msg == expected_empty_cart_msg'''






if __name__ == '__main__':
    unittest.main()
