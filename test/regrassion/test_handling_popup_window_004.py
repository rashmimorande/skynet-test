import unittest
from app.utils import create_driver_instance
from app.ui.mobile_page import MobilePage
from app.ui.home_page import HomePage
from app.ui.product_compare_page import ProductComparePage

import time

class Test_handling_popup(unittest.TestCase):


    def setUp(self):
        self.browser = create_driver_instance.get_driver_instance()
        self.mobile_page = MobilePage(self.browser)
        self.home_page = HomePage(self.browser)
        self.product_compare_page = ProductComparePage(self.browser)


    def tearDown(self):
        self.browser.close()

    def test_handling_popup_window(self):
        # step 1 click on mobile link
        self.home_page.get_mobile().click()
        #seep 2 in mobile product list click on "add to compare for two mobiles"
        self.mobile_page.get_add_to_compare_sonyxperia().click()
        self.mobile_page.get_add_to_compare_iphone().click()
        self.mobile_page.get_compare_button().click()
        #step 3 switch to  popup
        multiple_window_handle=self.browser.window_handles
        parent_window=multiple_window_handle[0]
        child_window=multiple_window_handle[1]
        self.browser.switch_to_window(child_window)
        self.browser.maximize_window()
        time.sleep(5)
        scroll_window = "window.scroll(0,500)"
        self.browser.execute_script(scroll_window)
        time.sleep(5)
        self.product_compare_page.get_close_window().click()
        self.browser.quit()




if __name__ == '__main__':
    unittest.main()
