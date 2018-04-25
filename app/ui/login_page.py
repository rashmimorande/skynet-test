from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage():
    def __init__(self,browser):
        self.browser = browser

    def wait_for_login_page_to_load(self):
        wait = WebDriverWait(self.browser,60)
        wait.until(expected_conditions.visibility_of(self.browser.find_element_by_xpath("//img[@title='Flipkart']")))

    def get_email_textbox(self):
        try:
            return self.browser.find_element_by_xpath("//span[contains(text(),'Enter Email/Mobile number')]/parent::label/preceding-sibling::input[@type='text']")
        except:
            return None

    def get_password_textbox(self):
        try:
            return self.browser.find_element_by_xpath("//span[contains(text(),'Enter Password')]/parent::label/preceding-sibling::input[@type='password']")
        except:
            return None

    def get_login_button(self):
        try:
            return self.browser.find_element_by_xpath("//span[contains(text(),'Login')]/parent::button[@type='submit']")
        except:
            return None

    def get_login_error_msg(self):
        try:
            return self.browser.find_element_by_xpath("//span[contains(text(),'Your username or password is incorrect')]")
        except:
            return None