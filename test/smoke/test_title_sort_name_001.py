#day1 guru99

import unittest
from app.utils import create_driver_instance
from app.ui.home_page import HomePage
from app.ui.mobile_page import MobilePage
import time

class Testmobilelistsorted_001(unittest.TestCase):

    def setUp(self):
        self.browser = create_driver_instance.get_driver_instance()
        self.home_page = HomePage(self.browser)
        self.mobile_page = MobilePage(self.browser)

    def tearDown(self):
        self.browser.close()

    def test_title(self):
        time.sleep(5)
        actual_title = self.browser.title
        expected_title = 'Home page'
        assert actual_title == expected_title
        self.home_page.get_mobile().click()
        time.sleep(5)
        actual_title1 = self.browser.title
        expected_title1 = 'Mobile'
        assert actual_title1 == expected_title1
        self.mobile_page.get_position().click()
        self.mobile_page.get_name().click()
        time.sleep(5)
        self.browser.save_screenshot("C:\\Users\\welcome\\PycharmProjects\\Directory\\skynet-test\\screenshots\\test1.png")



    '''def test_sort_by_name(self):
        #name_ddl = self.browser.find_element_by_css_selector("//div[@class='category-products']/div[@class='toolbar']/div[@class='sorter']/div[@class='sort-by']/child::select").click()
        name_ddl=self.browser.find_element_by_css_selector("select[title=\"Sort By\")
        name_sct = Select(name_ddl)
        name_sct.select_by_value('http://live.guru99.com/index.php/mobile.html?dir=asc&order=name') '''






if __name__ == '__main__':
    unittest.main()
