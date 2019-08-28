# -*- coding:utf-8 -*-
from selenium import webdriver

url = 'http://www.baidu.com/'

driver = webdriver.Chrome()
driver.get(url)
print(driver.page_source)