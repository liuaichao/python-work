# -*- coding:utf-8 -*-
import requests
from lxml import etree
from urllib import request
import time
from selenium import webdriver
import socket
import csv
import logging
import random
logging.captureWarnings(True)
def yel(url, title1, headers):
    # headers = {
    #     'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    #     'Connection': 'close'
    # }
    # time.sleep(2)
    logging.captureWarnings(True)
    reqs = requests.get(url, headers=headers, verify=False)
    time.sleep(1)
    # print(reqs.text)
    res = etree.HTML(reqs.text)
    url2 = res.xpath('//ul[@class="playul"]/li/a/@href')
    url2s = url2[3]
    urlss = 'https://www.787zh.com'+url2s
    # print(urlss)
    reqss = requests.get(urlss, headers=headers, verify=False)
    # time.sleep(0.5)
    r = reqss.text
    b = r.encode('ISO-8859-1').decode(reqss.apparent_encoding)
    ress = etree.HTML(b)
    url3 = ress.xpath('//div[@class="download"]/a/@href')[0]
    # print(url3)
    # print(url3[0])
    #构建csv文件
    csv_url = [str(title1), str(url3)]
    with open('yello_url.csv', 'a') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(csv_url)
    # return csv_url

def wr_csv():
    pass
if __name__ == '__main__':
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

    base_url = ['https://www.787zh.com/vod/html23/','https://www.787zh.com/vod/html24/','https://www.787zh.com/vod/html25/']
    csv_urls = []
    # base_url = 'https://www.713zh.com/vod/html17/'
    for z in base_url:
        url_all = [str(z)]
        req = requests.get(z, headers=headers, verify=False)
        # time.sleep(1)
        r = req.text
        b = r.encode('ISO-8859-1').decode(req.apparent_encoding)
        xa = etree.HTML(b)
        xayi = xa.xpath('//ul/li/a[@class="disabled"]/@href')[1]
        panduan = xa.xpath('//ul/li[@class="visible-xs active"]//text()')
        panduan = panduan[0].split('/')[-1]
        # print(panduan)  /vod/html23/index_2.html
        # print(xayi)    https://www.713zh.com/vod/html23/
        xayi1 = xayi.split('_')[0]
        xayi2 = xayi.split('index')[0]
        # print(panduan)
        for x in range(int(panduan)-1):
            if x == 0:
                pass
            else:
                url_all.append(str('https://www.787zh.com'+str(xayi1)+str('_')+str(x)+str('.html')))

        # print(url_all)
        # print(len(url_all))
        for s in url_all:
            rem = requests.get(s, headers=headers, verify=False)
            # time.sleep(1)
            q = rem.text
            d = q.encode('ISO-8859-1').decode(rem.apparent_encoding)
            ht = etree.HTML(d)
            urls = ht.xpath('//ul[@class="clearfix"]/li/a/@href')
            title = ht.xpath('//div[@class="title"]/h5/a')
            # title = [i for i in range(100)]
            for i,j in zip(urls,title):
                # time.sleep(2)
                url = 'http://www.787zh.com/'+i
                title1 = j.text
                print(title1)
                # print(url)
                # time.sleep(1)
                yel(url, title1, headers)
                # csv_urls.append(ret)
                # print(csv_urls)
    # with open('yello_url.csv', 'w') as f:
    #     f_csv = csv.writer(f)
    #     f_csv.writerows(csv_urls)