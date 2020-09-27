# -*- coding:utf-8 -*-
import requests
from lxml import etree
from requests.adapters import HTTPAdapter
import time

s = requests.Session()
import os
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))

headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400',
            }


urls = ["https://www.15y.tv/Pic/index_{0}.html".format(i) for i in range(80,85)]
print(urls)

url_list = []
name_list = []
#图片下载
def st(photo_url, headers, m):
    if os.path.exists("D:\\photo_yellow\\" + m):
        pass
    else:
        os.mkdir("D:\\photo_yellow\\" + m)

    res = s.get(photo_url, headers=headers)
    file_na = photo_url.split('/')[-1]
    with open('D:\photo_yellow\\'+str(m)+'\\'+str(file_na), 'wb') as f:
        f.write(res.content)

#获取url
for url in urls:
    rep = s.get(url=url, headers=headers)
    html = rep.text
    b = html.encode('ISO-8859-1').decode(rep.apparent_encoding)
    xa = etree.HTML(b)
    url_list_a = xa.xpath('//div[@class="list"]/ul/li/a/@href')
    for i in range(len(url_list_a)):
        url_list_a[i] = "https://www.15y.tv/"+url_list_a[i]

    # print(url_list_a)
    name = xa.xpath('//div[@class="list"]/ul/li/a/@title')
    for i in range(len(name)):
        name[i] = name[i].strip().replace(" ", "")
    # print(name)
    url_list = url_list_a + url_list
    name_list = name + name_list

print(url_list)
print(name_list)
#每页图片
for i in range(len(url_list)):
    print("开始:{}".format(url_list[i]))
    time.sleep(0.3)
    rep = s.get(url=url_list[i], headers=headers)
    html = rep.text
    b = html.encode('ISO-8859-1').decode(rep.apparent_encoding)
    xa = etree.HTML(b)
    url_photo_list = xa.xpath('//div[@class="jianjie img"]/img/@src')
    for url_photo in url_photo_list:
        print("开始下载-------{}".format(name_list[i]))
        st(url_photo, headers, name_list[i])

        #print("liuaichao1234567890")
        #print("zxcvbnmasdfghjklqwertyuio")
        # a = lambda x: x+1
