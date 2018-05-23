
class MobileDescriptionPageSonyxperia():
    def __init__(self, browser):
        self.browser = browser

    def get_sonyxperia(self):
        try:
            return self.browser.find_element_by_xpath("//span[contains(text(),'Sony Xperia')]")
        except:
            return None

    def get_price_sonyxperia(self):
        try:
            return self.browser.find_element_by_xpath("//span[contains(text(),'$100.00')]")
        except:
            return None

    def get_qty_sonyxperia(self):
        try:
            return self.browser.find_element_by_xpath("//div[@class='qty-wrapper']/input[@id='qty']")
        except:
            return None

    def get_edit_sonyxperia(self):
        try:
            return self.browser.find_element_by_xpath("//input[@type='text']/parent::td/ul[@class='cart-links']/li/a[contains(text(),'Edit')]")
        except:
            return None

    def get_update_button(self):
        try:
            return self.browser.find_element_by_xpath("//div[@class='add-to-cart-buttons']/button/span/span[contains(text(),'Update Cart')]")
        except:
            return None

    def get_error_msg(self):
        try:
            return self.browser.find_element_by_xpath("//ul[@class='messages']/li/ul/li/span[contains(text(),'The maximum quantity allowed for purchase is 500.')]")
        except:
            return None

    def get_empty_cart(self):
        try:
            return self.browser.find_element_by_xpath("//td[@class='a-right cart-footer-actions last']/button[@id='empty_cart_button']/span/span[contains(text(),'Empty Cart')]")
        except:
            return None

    def get_empty_cart_msg(self):
        try:
            return self.browser.find_element_by_xpath("//h1[contains(text(),'Shopping Cart is Empty')]")
        except:
            return None







