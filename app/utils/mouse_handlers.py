
from selenium.webdriver import ActionChains


def mouse_hover_on_element(browser,element):
    act=ActionChains(browser)
    act.move_to_element(element).perform()


def drag_and_drop_elements(browser, src_element, target_element):
    act=ActionChains(browser)
    act.drag_and_drop(src_element,target_element).perform()


def right_click_on_element(browser, element):
    act=ActionChains(browser)
    act.context_click(element).perform()

