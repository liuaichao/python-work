# -*- coding:utf-8 -*-
import requests
from lxml import etree
from urllib import request
import time
from selenium import webdriver
import socket

def Schedule(blocknum, blocksize, totalsize):
    per = 100*blocknum*blocksize/totalsize
    print("当前下载进度为:{0}".format(per))

def yel(url, title1):
    headers = {
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
    # time.sleep(2)
    reqs = requests.get(url, headers)
    time.sleep(1)
    # print(reqs.text)
    res = etree.HTML(reqs.text)
    url2 = res.xpath('//ul[@class="playul"]/li/a/@href')
    url2s = url2[3]
    urlss = 'https://www.787zh.com'+url2s
    # print(urlss)
    reqss = requests.get(urlss, headers)
    time.sleep(1)
    r = reqss.text
    b = r.encode('ISO-8859-1').decode(reqss.apparent_encoding)
    ress = etree.HTML(b)
    url3 = ress.xpath('//div[@class="download"]/a/@href')
    # print(url3[0])
    #构建filename
    file_name = 'D:\yello\\'+title1+'.mp4'
    # print(file_name)
    try:
        request.urlretrieve(url3[0],file_name,Schedule)
    except socket.timeout:
        count = 1
        while count <= 5:
            try:
                request.urlretrieve(url3[0], 'D:\yello\\' + title1 + '.mp4', Schedule)
                break
            except socket.timeout:
                err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                print(err_info)
                count += 1
        if count > 5:
            print("下载失败")
if __name__ == '__main__':

    headers = {
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
    base_url = 'https://www.787zh.com/vod/html18/'
    # base_url = 'https://www.797zh.com/vod/html19/'
    url_all = ['https://www.787zh.com/vod/html18/']
    req = requests.get(base_url, headers=headers)
    time.sleep(1)
    r = req.text
    b = r.encode('ISO-8859-1').decode(req.apparent_encoding)
    xa = etree.HTML(b)
    xayi = xa.xpath('//ul/li/a[@class="disabled"]/@href')[1]
    panduan = xa.xpath('//ul/li[@class="visible-xs active"]//text()')
    panduan = panduan[0].split('/')[-1]
    # print(panduan)
    # print(xayi)
    for x in range(int(panduan)-1):
        url_all.append(str('https://www.787zh.com'+xayi))

    print(url_all)
    for s in url_all:
        rem = requests.get(s, headers=headers)
        time.sleep(1)
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
            print(url)
            time.sleep(1)
            yel(url, title1)