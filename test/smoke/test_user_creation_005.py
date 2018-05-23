import unittest
from app.utils  import create_driver_instance
import time


class Test_user_creation(unittest.TestCase):

    def setUp(self):
        self.browser=create_driver_instance.get_driver_instance()

    def tearDown(self):
        self.browser.close()

    def test_user_creation_005(self):
        #step 1 click on account
        self.browser.find_element_by_xpath("//div[@class='account-cart-wrapper']/a/span[contains(text(),'Account')]").click()
        #self.browser.find_element_by_xpath("//div[@id='header-account']/div/ul/li/a[contains(text(),'My Account')]").click()

        #step 2 click on create and account and fill the info
        #self.browser.find_element_by_xpath("//div[@class='buttons-set']/a/span/span[contains(text(),'Create an Account')]").click()
        #self.browser.find_element_by_id("firstname").send_keys("rash1")
        #self.browser.find_element_by_id("lastname").send_keys("moru1")
        #self.browser.find_element_by_id("email_address").send_keys("rash.morande@gmail.com")
        #self.browser.find_element_by_id("password").send_keys("123456")
        #self.browser.find_element_by_id("confirmation").send_keys("123456")
        #self.browser.find_element_by_xpath("//div[@class='buttons-set']/button/span/span[contains(text(),'Register')]").click()
        self.browser.find_element_by_xpath("//div[@id='header-account']/div/ul/li/a[contains(text(),'Log In')]").click()
        self.browser.find_element_by_id("email").send_keys("rashmi.morande@gmail.com")
        self.browser.find_element_by_id("pass").send_keys("123456")
        self.browser.find_element_by_xpath("//div[@class='buttons-set']/button/span/span[contains(text(),'Login')]").click()
        #time.sleep(5)
        #verify_registration=self.browser.find_element_by_xpath("//div[@class='header-language-background']/div/p[contains(text(),'Welcome, Rashmi Morande! ')]")

        #verify_registration.text
        #expected_verify_registration = 'WELCOME, RASHMI MORANDE!'
        #assert verify_registration==expected_verify_registration

        #step 3 go to tv menu
        self.browser.find_element_by_xpath("//div[@id='header-nav']/nav/ol/li/a[contains(text(),'TV')]").click()
        self.browser.find_element_by_xpath("//div[@class='actions']/ul/li/a[contains(text(),'Add to Wishlist')]").click()
        self.browser.find_element_by_xpath("//div[@class='buttons-set buttons-set2']/button/span/span[contains(text(),'Share Wishlist')]").click()
        self.browser.find_element_by_id("email_address").send_keys("rashmorande@gmail.com")
        self.browser.find_element_by_id("message").send_keys("this is my wishlist")
        self.browser.find_element_by_xpath("//div[@class='buttons-set form-buttons']/button/span/span[contains(text(),'Share Wishlist')]").click()
        actual_msg = self.browser.find_element_by_xpath("//span[contains(text(),'Your Wishlist has been shared')]")
        time.sleep(5)
        msg = actual_msg.text
        print ("msg")







if __name__ == '__main__':
    unittest.main()
