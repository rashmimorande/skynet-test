import unittest
from app.utils import create_driver_instance
from app.utils import drop_down_handlers
import time
from selenium.webdriver.support.select import Select

class Test_purchase_product(unittest.TestCase):

    def setUp(self):
        self.browser=create_driver_instance.get_driver_instance()


    '''def tearDown(self):
        self.browser.close()'''

    def test_purchase_product_006(self):
        #step 1, 2, 3
        self.browser.find_element_by_xpath("//div[@class='account-cart-wrapper']/a/span[contains(text(),'Account')]").click()
        self.browser.find_element_by_xpath("//div[@id='header-account']/div/ul/li/a[contains(text(),'Log In')]").click()
        self.browser.find_element_by_id("email").send_keys("rashmi.morande@gmail.com")
        self.browser.find_element_by_id("pass").send_keys("123456")
        self.browser.find_element_by_xpath("//div[@class='buttons-set']/button/span/span[contains(text(),'Login')]").click()

        #step 4 click on my wishlist
        self.browser.find_element_by_xpath("//div[@class='block-content']/ul/li/a[contains(text(),'My Wishlist')]").click()
        #step 5 click on proced to checkout
        self.browser.find_element_by_xpath("//div[@class='cart-cell']/button/span/span[contains(text(),'Add to Cart')]").click()

        #step 8
        state_ddl = self.browser.find_element_by_id('region_id')
        state_sct = Select(state_ddl)
        state_sct.select_by_visible_text('New York')
        self.browser.find_element_by_id('postcode').send_keys("542896")
        self.browser.find_element_by_xpath("//button[@title='Estimate']/span/span[contains(text(),'Estimate')]").click()
        self.browser.find_element_by_xpath("//button[@title='Update Total']/span/span[contains(text(),'Update Total')]").click()
        scroll1 = "window.scroll(0,200)"
        self.browser.execute_script(scroll1)
        sub_total = self.browser.find_element_by_xpath("//td[@class='a-right']/span[contains(text(),'$615.00')]")

        #float(sub_total)
        shipping_total = self.browser.find_element_by_xpath("//td[@class='a-right']/span[contains(text(),'$5.00')]")
        #float(shipping_total)
        #time.sleep(5)
        #sub_total_value = sub_total.text
        #time.sleep(5)
        #shipping_total_value = shipping_total.text
        #total = sub_total_value + shipping_total_value
        actual_grand_total = self.browser.find_element_by_xpath("//td[@class='a-right']/strong/span[contains(text(),'$620.00')]")
        expected_grand_total = '$620.00'
        #time.sleep(5)
        #grand_total_value = grand_total.text
        assert actual_grand_total == expected_grand_total

        self.browser.find_element_by_xpath("//div[@class='page-title title-buttons']/ul/li/button/span/span[contains(text(),'Proceed to Checkout')]").click()
        #step 6 enter shipping information
        #self.browser.find_element_by_id("billing:firstname").send_keys("Rashmi")
        #self.browser.find_element_by_id("billing:lastname").send_keys("Morande")
        self.browser.find_element_by_id("billing:street1").send_keys("ABC")
        self.browser.find_element_by_id("billing:city").send_keys("newyork")
        scroll="window.scroll(0,500)"
        self.browser.execute_script(scroll)

        element_ddl = self.browser.find_element_by_id("billing:region_id")
        #drop_down_handlers.select_ddl_by_visible_text(element_ddl, 'New York')
        sct=Select(element_ddl)
        sct.select_by_visible_text("New York")
        self.browser.find_element_by_id("billing:postcode").send_keys("542896")
        country_ddl=self.browser.find_element_by_id("billing:country_id")
        sct1=Select(country_ddl)
        sct1.select_by_visible_text("United States")
        self.browser.find_element_by_id("billing:telephone").send_keys("12345678")
        self.browser.find_element_by_xpath("//button[@title='Continue']/span/span[contains(text(),'Continue')]").click()














if __name__ == '__main__':
    unittest.main()
