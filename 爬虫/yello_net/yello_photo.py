# -*- coding:utf-8 -*-
import requests
from lxml import etree
from urllib import request
import time
from selenium import webdriver
import socket
import csv
import random
import os
def st(photo_url, headers, m):
    res = requests.get(photo_url, headers=headers)
    file_na = photo_url.split('/')[-1]
    with open('D:\python程序\爬虫\yello_net\\'+str(m)+'\\'+str(file_na), 'wb') as f:
        f.write(res.content)



if __name__ == '__main__':
    base_url = 'https://www.713zh.com/pic/html28/'
    head = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",

            ]
    headers = {
        'User - Agent': str(random.choice(head)),
        'Connection': 'close'
    }
    url_all = []
    req = requests.get(base_url, headers=headers)
    time.sleep(1)
    r = req.text
    b = r.encode('ISO-8859-1').decode(req.apparent_encoding)
    xa = etree.HTML(b)

    panduan = xa.xpath('//ul/li[@class="visible-xs active"]//text()')
    panduan = panduan[0].split('/')[-1]
    # print(xayi)
    # print(panduan)
    for i in range(int(panduan)-1):
        if i == 0:
            url_all.append(str('https://www.787zh.com/pic/html28/'))
        else:
            url_all.append(str('https://www.787zh.com/pic/html28/index_'+str(i))+str('.html'))
    print(url_all)
    for j in url_all:
        res = requests.get(j, headers=headers)
        time.sleep(1)
        r = res.text
        b = r.encode('ISO-8859-1').decode(res.apparent_encoding)
        xa = etree.HTML(b)
        wenjian_name = xa.xpath('//ul[@class="box-topic-list p-0 clearfix"]/li/a/@title')
        wenjian_url = xa.xpath('//ul[@class="box-topic-list p-0 clearfix"]/li/a/@href')
        for m,n in zip(wenjian_name,wenjian_url):
            res = requests.get('https://www.830zh.com'+n, headers=headers)
            time.sleep(1)
            r = res.text
            b = r.encode('ISO-8859-1').decode(res.apparent_encoding)
            xa = etree.HTML(b)
            photo_urls = xa.xpath('//div[@class="details-content text-justify"]/img/@src')
            if os.path.exists(m):
                continue
            else:
                os.mkdir(m)
            for photo_url in photo_urls:
                st(photo_url, headers, m)

