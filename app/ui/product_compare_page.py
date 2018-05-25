
class ProductComparisionPage():
    def __init__(self,browser):
        self.browser = browser

    def get_compare_product(self):
        try:
            return self.browser.find_element_by_xpath("//h1[contains(text(),'Compare Products')]")
        except:
            return None
    def get_close_window(self):
        try:
            return self.browser.find_element_by_xpath("//span[contains(text(),'Close Window')]")
        except:
            return None
