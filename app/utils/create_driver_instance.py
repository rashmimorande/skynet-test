import pytest
from selenium.webdriver import Firefox, Chrome, Ie
import pytest

def get_driver_instance():
    type = pytest.config.option.type
    env = pytest.config.option.env
    if env == 'local':
        if type.lower() == 'firefox':
            browser = Firefox()
        elif type.lower() == 'chrome':
            browser = Chrome("./skynet-test/browser-server/chromedriver.exe")
        elif type.lower() == 'ie':
            browser = Ie("./skynet-test/browser-server/IEDriverServer.exe")
    elif env == 'remote':
        print('running on remote env')
    browser.maximize_window()
    browser.implicitly_wait(30)
    browser.get("http://live.guru99.com/index.php/")
    return browser
