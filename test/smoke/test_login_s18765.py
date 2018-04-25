

import unittest
import json
from app.ui.login_page import LoginPage
from app.utils import create_driver_instance


class TestLoginS18765(unittest.TestCase):

    def setUp(self):
        self.browser = create_driver_instance.get_driver_instance()
        self.login_page = LoginPage(self.browser)
        self.test_data = json.load(open("./skynet-test/test/smoke/s18765.json",'r'))

    def tearDown(self):
        self.browser.close()

    def test_login_invalid_tc15462(self):
        self.login_page.wait_for_login_page_to_load()
        self.login_page.get_email_textbox().send_keys(self.test_data['valid_username'])
        self.login_page.get_password_textbox().send_keys(self.test_data['invalid_password'])
        self.login_page.get_login_button().click()
        actual_error_msg = self.login_page.get_login_error_msg().text
        expected_error_msg = 'Your username or password is incorrect'
        assert actual_error_msg == expected_error_msg


if __name__ == '__main__':
    unittest.main()
