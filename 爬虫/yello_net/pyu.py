# -*- coding:utf-8 -*-
import requests
from lxml import etree
url = 'https://www.787zh.com/pic/html28/'
req = requests.get(url)
html = etree.HTML(req.text)
html = html.xpath('//ul/li/a/@data-original')
# title = html.xpath('//ul/li/a/span')
for i in zip(html):
    print(i)
    # print(j)
    # with open('','wb') as f:
    #     f.write(f)
