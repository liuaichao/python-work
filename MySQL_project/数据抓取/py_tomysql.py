# -*- coding:utf-8 -*-
import requests
from lxml import etree
from 爬虫.UserAgent_demo import UserAgent
import random
import re
from MySQL_project.数据抓取.mysql_demo import Mysql_demo
import time
USER = UserAgent()

#得到书名，内容。。。
def get_page_url(url,USER):

    is_next = True
    headers = {
        'Referer':'http://www.bookschina.com/',
        'Host':'www.bookschina.com',
        'User-Agent': random.choice(USER.getuseragent())
    }
    time.sleep(random.choice([0.3,0.5,0.7,1,1.3,1.6,1.9,2]))
    req = requests.get(url,headers=headers)
    html = req.text
    html = etree.HTML(html)
    #标题
    title = html.xpath('//div[@class="bookList"]/ul/li/div[@class="infor"]/h2/a/@title')
    #作者
    author = html.xpath('//div[@class="bookList"]/ul/li/div[@class="infor"]/div[@class="otherInfor"]/a[1]/text()')
    #出版社
    publisher = html.xpath('//div[@class="bookList"]/ul/li/div[@class="infor"]/div[@class="otherInfor"]/a[2]/text()')
    if len(title) != len(publisher):
        return
    #内容
    recolagu = re.findall(r'<p class="recoLagu">([\s\S]*?)</p>',req.text)
    #购买链接
    href = html.xpath('//div[@class="infor"]/h2/a/@href')
    #类型
    drop_type = html.xpath('//div[@class="dropMenu"]/a/text()')
    if len(title) != len(recolagu):
        return
    #得到下一页信息
    try:
        next_page = html.xpath('//li[@class="next"]/a/@href')
        next_page = 'http://www.bookschina.com'+next_page[0]
    except:
        is_next = False
    #数据处理部分
    for i in range(int(len(title))):
        title[i] = title[i].strip().replace(' ','')
        author[i] = author[i].strip().replace(' ','')
        publisher[i] = publisher[i].strip().replace(' ','')
        recolagu[i] = recolagu[i].strip().replace(' ','')
        href[i] = 'http://www.bookschina.com'+href[i].strip().replace(' ','')
    print(title)
    #数据存储
    try:
        mysql = Mysql_demo()
    except:
        time.sleep(4)
        try:
            mysql = Mysql_demo()
        except:
            time.sleep(4)
            try:
                mysql = Mysql_demo()
            except:
                mysql = Mysql_demo()
    for i in range(len(title)):
        sql = 'insert into book(title,author,publisher,recolagu,href,drop_type) values ("{0}","{1}","{2}","{3}","{4}","{5}");'.format(title[i],author[i],publisher[i],recolagu[i],href[i],drop_type[0])
        mysql.insert(sql)

    if is_next == False:
        return

    get_page_url(next_page,USER)


if __name__ == '__main__':
    USER = UserAgent()
    headers = {
        'Referer':'http://www.bookschina.com/',
        'Host':'www.bookschina.com',
        'User-Agent': random.choice(USER.getuseragent())
    }
    req = requests.get('http://www.bookschina.com/', headers=headers)
    html = etree.HTML(req.text)
    urls = html.xpath('//p[@class="mcate-item-bd"]//a/@href')
    for i in range(len(urls)):
        urls[i] = 'http://www.bookschina.com' + urls[i]
    for i in range(len(urls)):
        try:
            USER = UserAgent()
        except:
            time.sleep(5)
            USER = UserAgent()


        if i>=230:
            print(i)
            print(urls[i])
            try:
                get_page_url(urls[i],USER)
            except:
                get_page_url(urls[i],USER)
