
from selenium.webdriver.support import select

def select_ddl_by_index(element_ddl,index):
    sct=select(element_ddl)
    sct.select_by_index(index)

def select_ddl_value(element_ddl,value):
    sct=select(element_ddl)
    sct.select_by_value(value)

def select_ddl_by_visible_text(element_ddl, text):
    sct=select(element_ddl)
    sct.select_by_visible_text(text)

def deselect_ddl_by_index(element_ddl,index):
    sct=select(element_ddl)
    sct.deselect_by_index(index)

def deselect_ddl_value(element_ddl,value):
    sct=select(element_ddl)
    sct.deselect_by_value(value)

def deselect_ddl_by_visible_text(element_ddl, text):
    sct=select(element_ddl)
    sct.deselect_by_visible_text(text)