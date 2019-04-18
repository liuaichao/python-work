# -*- coding:utf-8 -*-
import requests
import json
import re
import os
from lxml import etree

headers = {
    'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}
url = 'https://www.bilibili.com/ranking?spm_id_from=333.334.b_62616e6e65725f6c696e6b.1'
req  = requests.get(url, headers = headers)
html = etree.HTML(req.text)
urls = html.xpath('//div[@class="img"]/a/@href')
names = html.xpath('//div[@class="info"]/a/text()')

path = 'D:\\python程序\\爬虫\\bilibili-you-get\\视频'
if not os.path.exists(path):
    os.mkdir(path)
for url,name in zip(urls,names):
    url = url.split('//')[-1]
    name = name.strip()
    path = path +'\\'+name
    print('正在下载：{0}'.format(name))
    os.system('you-get -o {0} {1}'.format(path, url))
    print('{0}---->下载完成'.format(name))