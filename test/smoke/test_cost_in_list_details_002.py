#day-2 guru99

import unittest
from app.utils import create_driver_instance
from app.ui.home_page import HomePage
from app.ui.mobile_page import MobilePage
from app.ui.mobile_description_page_sonyxperia import MobileDescriptionPageSonyxperia


class Test_costofmobile_002(unittest.TestCase):

    def setUp(self):
        # 1. Go to http://live.guru99.com
        self.browser=create_driver_instance.get_driver_instance()
        self.mobile_page = MobilePage(self.browser)
        self.home_page = HomePage(self.browser)
        self.mobile_description_page = MobileDescriptionPageSonyxperia(self.browser)

    def tearDown(self):
        self.browser.close()

    def test_cost_002(self):

        # 2. Click on Mobile menu
        self.home_page.get_mobile().click()
        # 3. In the  list of all mobile , read the cost of Sony Xperia mobile (which is $100)
        price_on_list_page = self.mobile_page.get_price_sonyxperia().text
        print(price_on_list_page)
        # 4. Click on Sony Xperia mobile
        self.mobile_page.get_sonyxperia().click()
        # 5. Read the XPeria mobile price from details page
        price_on_description_page = self.mobile_description_page.get_price_sonyxperia().text
        print(price_on_description_page)
        # 6. compare value in step 3 and step 5
        assert price_on_list_page == price_on_description_page


if __name__ == '__main__':
    unittest.main()










