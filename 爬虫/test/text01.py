# -*- coding:utf-8 -*-
from selenium import webdriver
import requests
from UserAgent_demo import UserAgent
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
a = UserAgent()
headers = {
    'Host':'www.aliexpress.com',
    'Referer':'https://www.aliexpress.com/',
    'Cookie':None,
    'User-Agent':random.choice(a.getuseragent()),

}
#
url = 'https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20190601224020&SearchText=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91'
#
# req = requests.get(url, headers=headers)
# print(req.text)
# html = etree.HTML(req.text)
# data = html.xpath('//div[@class="item"]/div[@class="info"]/h3/a/@href')
# print(data)
url = 'https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=1&sess=1&pid=11118004&rp=99999'

driver = webdriver.Chrome()
driver.get(url)
print(driver.page_source)
# time.sleep(20)
# driver.get(url)
# time.sleep(10)
# print(driver.page_source)
html = etree.HTML(driver.page_source)
# data = html.xpath('//div[@class="item"]/div[@class="info"]/h3/a/@href')
data2 = html.xpath('//dd[@class="box_card_img"]/img/@src')
# data2 = [data1.text for data1 in data2]
print(data2)
# print(len(data2))
# print(data)
# print(len(data))
driver.quit()

