# -*- coding:utf-8 -*-
import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'
}
req = requests.get('http://www.qlu.edu.cn/38/list.htm',headers=headers)

html = req.text
print(html)
# html = etree.HTML(html)
# title = html.xpath('//ul/li/span/a/@title')
# print(title)