#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author zzk
import urllib.request
import urllib.parse
import json
import random
import time
import pymysql
import csv
import pandas as pd
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
            for data in datas:
                # 职位名称
                zwmcs = data['jobName']
                # 公司名称
                gsmcs = data['company']['name']
                #公司类型
                gslxs = data['company']['type']['name']
                #公司规模
                gsgms= data['company']['size']
                #发布时间
                fbsjs = data['updateDate']
                # 职位月薪
                zwyxs = data['salary']
                #工作要求
                gzyqs = data['eduLevel']['name']
                # 工作地点
                gzdds = data['city']['display']
                #工作类型
                gzlxs = data['jobType']['items'][0]['name']
                # 待遇
                gxsjs = data['welfare'][0:]
                g=''
                for i in gxsjs:
                    g+=i
                gxsjs=g
                #经验
                jys = data['workingExp']['name']


                # item = {
                #     '职位名称':zwmcs,
                #     '公司类型':gslxs,
                #     '公司规模':gsgms['name'],
                #     '发布时间':fbsjs,
                #     '工作要求':gzyqs,
                #     '工作类型':gzlxs,
                #     '工作经验':jys,
                #     '公司名称': gsmcs,
                #     '职位月薪': zwyxs,
                #     '工作地点': gzdds,
                #     '公司待遇': gxsjs
                # }
                try:
                    data = [zwmcs, gslxs, gsgms['name'], fbsjs, gzyqs, gzlxs, jys, gsmcs,
                          zwyxs, gzdds, gxsjs]
                    print(data)
                    with open('./baomu.csv', 'a+', encoding='utf_8_sig', newline='') as f:
                        f_csv = csv.writer(f)
                        f_csv.writerow(data)
                except:
                    pass



    #爬取程序
    def run(self):
        for page in range(self.start_page,self.end_page+1):
            print('开始爬取第%s页' % page)
            self.handle_request(page*90)#成员方法可以访问成员属性,类属性
            #发送请求获取内容
            content = urllib.request.urlopen(self.request).read().decode()
            #解析内容
            self.parse_content(content)
            print('结束爬取第%s页'%page)
            # with open ('./zhilian.txt','w',encoding='utf-8') as fp:
            #     fp.write(str(self.items))
            time.sleep(random.uniform(0, 1.5) )


def main():
    # jl = input('输入工作地点：')
    jl = '不限'
    kw = input('请输入关键字：')
    # start_page = int(input('输入起始页码：'))
    # end_page = int(input('输入结束页码：'))
    start_page = 1
    end_page = 11
    #创建对象，启动爬取程序
    with open('./data.csv', 'a+', encoding='utf_8_sig',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(['职位名称','公司类型','公司规模','发布时间','工作要求','工作类型',
                        '工作经验','公司名称','职位月薪','工作地点','公司待遇'])
    spider = ZhiLianSpider(jl,kw,start_page,end_page)
    spider.run()
main()