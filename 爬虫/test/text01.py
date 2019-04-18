# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(browser, 10)  # 超时时长为10s
browser.get('https://www.taobao.com/')
print(browser.page_source)