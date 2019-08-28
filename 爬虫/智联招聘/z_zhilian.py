#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author zzk
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json
import time
class ZhiLianSpider(object):
    #拼接url
    url = 'https://fe-api.zhaopin.com/c/i/sou?'
    def __init__(self,jl,kw,start_page,end_page):
        self.jl = jl
        self.kw = kw
        self.start_page = start_page
        self.end_page = end_page
        self.items =[]#存放所有工作信息
    #拼接url生成请求对象:
    def handle_request(self,start,pageSize='90'):
        data ={
            'start': start,
            'pageSize': pageSize,
            'cityId':self.jl,
            'kw':self.kw,
            'kt':'3'

        }
        url_now = self.url+ urllib.parse.urlencode(data)
        print(url_now)
        #构建请求对象
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400',
        }
        self.request = urllib.request.Request(url=url_now, headers=headers)
    #解析内容函数
    def parse_content(self,content):
        rsp = urllib.request.urlopen(self.request)
        html = rsp.read().decode()
        te = json.loads(html)
        datas = te['data']['results']
        # print(datas)
        # zwmcs = []
        # gsmcs = []

        for data in datas:
            # 职位名称
            zwmc = data['jobName']
            # 公司名称
            gsmc = data['company']['name']
            # 职位月薪
            zwyx = data['salary']
            # 工作地点
            gzdd = data['city']['display']
            # 待遇
            gxsj = data['welfare']
            item = {
                '职位名称': zwmc,
                '公司名称': gsmc,
                '职位月薪': zwyx,
                '工作地点': gzdd,
                '公司待遇': gxsj
            }  # 存放入列表
            self.items.append(item)
            # print(zwmc,gsmc,zwyx,gzdd,gxsj)
        # soup =BeautifulSoup(content,'lxml')
        # print(soup)
        # zwmc = soup.select('span[class="contentpile__content__wrapper__item__info__box__jobname__title"]')#职位名称
        # print(zwmc)
        # gsmc = soup.select('.contentpile__content__wrapper__item__info__box__cname commpanyName> a')[0].text#公司名称
        # zwyx = soup.select('contentpile__content__wrapper__item__info__box__job__saray')[0].text#职位月薪
        # gzdd = soup.select('.contentpile__content__wrapper__item__info__box__job__demand__item')[0].text#工作地点
        # gxsj = soup.select('.contentpile__content__wrapper__item__info__box__welfare__item')[0:].text#待遇
        # for a,b,c,d,e in zip(zwmc,gsmc,zwyx,gzdd,gxsj):
        #     item ={
        #         '职位名称':a,
        #         '公司名称':b,
        #         '职位月薪':c,
        #         '工作地点':d,
        #         '公司待遇':e
        #     }#存放入列表
        #     self.items.append(item)
    #爬取程序
    def run(self):
        for page in range(self.start_page,self.end_page+1):
            print('开始爬取第%s页' % page)
            self.handle_request(page*90+90)#成员方法可以访问成员属性,类属性
            #发送请求获取内容
            content = urllib.request.urlopen(self.request).read().decode()
            #解析内容
            self.parse_content(content)
            print('结束爬取第%s页'%page)
            # string = json.dumps(self.items)
            with open ('./zhilian.txt','w',encoding='utf-8') as fp:
                fp.write(str(self.items))
                time.sleep(1)


def main():
    jl = input('输入工作地点：')
    kw = input('请输入关键字：')
    start_page = int(input('输入起始页码：'))
    end_page = int(input('输入结束页码：'))
    #创建对象，启动爬取程序
    spider = ZhiLianSpider(jl,kw,start_page,end_page)
    spider.run()
main()