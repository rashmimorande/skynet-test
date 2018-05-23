


class MobilePage():
    def __init__(self, browser):
        self.browser = browser

    def get_position(self):
        try:
            return self.browser.find_element_by_xpath("//select[@title='Sort By']/option[contains(text(),'Position')]")
        except:
            return None

    def get_name(self):
        try:
            return self.browser.find_element_by_xpath("//select[@title='Sort By']/option[contains(text(),'Name')]")
        except:
            return None

    def get_sonyxperia(self):
        try:
            return self.browser.find_element_by_xpath("//a[contains(text(),'Sony Xperia')]")
        except:
            return None

    def get_price_sonyxperia(self):
        try:
            return self.browser.find_element_by_xpath("//span[contains(text(),'$100.00')]")
        except:
            return None

    def get_add_to_cart_sonyxperia(self):
        try:
            return self.browser.find_element_by_xpath("// a[@title='Sony Xperia']/parent::h2/following-sibling::div[@class='actions']/button[@title='Add to Cart']")
        except:
            return None

    def get_add_to_compare_sonyxperia(self):
        try:
            return self.browser.find_element_by_xpath("//div[@class='product-info']/h2/a[contains(text(),'Sony Xperia')]/parent::h2/following-sibling::div[@class='actions']/ul/li/a[contains(text(),'Add to Compare')]")
        except:
            return None

    def get_add_to_compare_iphone(self):
        try:
            return self.browser.find_element_by_xpath("//div[@class='product-info']/h2/a[contains(text(),'IPhone')]/parent::h2/following-sibling::div[@class='actions']/ul/li/a[contains(text(),'Add to Compare')]")
        except:
            return None

    def get_compare_button(self):
        try:
            return self.browser.find_element_by_xpath("//div[@class='block block-list block-compare']/div[@class='block-content']/div/button/span/span[contains(text(),'Compare')]")
        except:
            return None


















