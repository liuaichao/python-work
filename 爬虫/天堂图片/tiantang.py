# -*- coding:utf-8 -*-
import requests
from urllib import request
from lxml import etree
import os
def Schedule(blocknum, blocksize, totalsize):
    '''

    :param blocknum:
    :param blocksize:
    :param totalsize:
    :return:
    '''
    per = 100.0*blocknum*blocksize/totalsize
    if per>100:
        per = 100
    print('当前下载进度为：{0}'.format(per))


urls = ['http://www.ivsky.com/tupian/zhiwuhuahui/','https://www.ivsky.com/tupian/ziranfengguang/']
try:
    os.mkdir('img')
except:
    pass
for url in urls:
    req = requests.get(url)
    html = etree.HTML(req.text)
    img_urls = html.xpath('//div[@class="il_img"]/a/img/@src')

    for img_url in img_urls:
        img_url = 'http:'+img_url
        filename = img_url.split('/')[-1]
        request.urlretrieve(img_url, 'img'+'/'+filename, Schedule)