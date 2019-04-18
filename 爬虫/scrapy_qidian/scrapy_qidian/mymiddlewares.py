# -*- coding:utf-8 -*-
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
class MKdownloadmiddleware(object):
    def __init__(self):
        pass
    def process_request(self, request, spider):
        print('启动webdriver')
        self.driver = webdriver.Chrome()
        self.driver.get(request.url)
        time.sleep(4)
        self.html = self.driver.page_source
        self.driver.quit()
        return HtmlResponse(url=request.url, encoding='utf-8', body=self.html, request=request)
