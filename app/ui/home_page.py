from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class HomePage():
    def __init__(self,browser):
        self.browser=browser

    def wait_for_home_page_to_load(self):
        wait=WebDriverWait(self.browser,60)
        wait.until(expected_conditions.visibility_of(self.browser.find_element_by_xpath("//p[contains(text(),'Default welcome msg! ')]")))

    def get_mobile(self):
        try:
            return self.browser.find_element_by_xpath("//a[contains(text(),'Mobile')]")
        except:
            return None


    def get_tv(self):
        try:
            return self.browser.find_element_by_xpath("//a[contains(text(),'Tv')]")
        except:
            return None


    def get_account(self):
        try:
            return self.browser.find_element_by_xpath("//div[@class='account-cart-wrapper']/a/span[contains(text(),'Account')]")
        except:
            return None






