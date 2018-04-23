import unittest

from app.utils import create_driver_instance

class TestTitle_s13976(unittest.TestCase):

    def setUp(self):
        self.browser=create_driver_instance.get_driver_instance()

    def tearDown(self):
        self.browser.close()

    def test_title_of_webpage_tc18796(self):
        actual_title=self.browser.title
        expected_title='Online Shopping Site for Mobiles, Fashion, Books, Electronics, Home Appliances and More'
        assert actual_title==expected_title


if __name__ == '__main__':
    unittest.main()
