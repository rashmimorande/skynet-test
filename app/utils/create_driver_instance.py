import pytest
from selenium.webdriver import Firefox, Chrome, Ie

def get_driver_instance():
    type=pytest.config.option.type
    env=pytest.config.option.env
    if env=='local':
        if type.lower()=='firefox':
            browser=Firefox()
        elif type.lower()=='chrome':
            browser=Chrome("./browser-server/chromedriver.exe")
        elif type.lower()=='ie':
            browser=Ie("./browser-server/IEDriverServer.exe")
    elif env=='remote':
        print('running on remote env')
    browser.maximize_window()
    browser.implicitly_wait(30)
    browser.get("https://www.flipkart.com")
    return browser

