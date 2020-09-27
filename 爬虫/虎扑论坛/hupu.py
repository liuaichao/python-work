# -*- coding:utf-8 -*-
import requests
from lxml import etree
from 爬虫 import mongo_demo
def to_mongo(data):
    mo = mongo_demo.MongoAPI('192.168.0.200', 27017,'虎扑','hupu')
    mo.add(data)


if __name__ == '__main__':
    url = 'https://bbs.hupu.com/vote'
    headers = {
        'User - Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'

    }
    req = requests.get(url, headers=headers)
    html = req.text
    html = etree.HTML(html)
    titles = html.xpath('//div[@class="show-list"]/ul//li/div[@class="titlelink box"]/a[@target="_blank"]')
    titles = [i.text for i in titles]
    del titles[0]
    # print(titles)
    zuozhes = html.xpath('//div[@class="show-list"]/ul//li/div[@class="author box"]/a[@target="_blank"]')
    zuozhes = [i.text for i in zuozhes]
    del zuozhes[0]
    times = html.xpath('//div[@class="author box"]/a[2]')
    times = [i.text for i in times]
    del times[0]
    liulans = html.xpath('//span[@class="ansour box"]/text()')
    liulan = [i.strip().split('\xa0/\xa0')[0] for i in liulans]
    pinglun = [i.strip().split('\xa0/\xa0')[1] for i in liulans]
    del liulan[0]
    del pinglun[0]
    huifu = html.xpath('//div[@class="endreply box"]/span/text()')
    del huifu[0]
    datas = zip(titles,zuozhes,times,liulan,pinglun,huifu)
    for i in datas:
        data = {
            '名称':i[0],
            '作者':i[1],
            '发布时间':i[2],
            '浏览量':i[3],
            '评论量':i[4],
            '最后回复者':i[5]
        }
        print(data)
        # to_mongo(data)


    # print(huifu)
    # print(liulan)
    # print(pinglun)
    # print(times)
    # print(titles)
    # print(zuozhes)
    # print(len(titles),len(zuozhes),len(times),len(liulan),len(pinglun),len(huifu))