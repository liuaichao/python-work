# -*- coding:utf-8 -*-
from 爬虫.Scrapy_xici.Scrapy_xici.my_pipelines.sql import Xicidaili_mysql
from 爬虫.Scrapy_xici.Scrapy_xici.items import XiciItem

class XiciPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, XiciItem):
            country = item['country']
            ip = item['ip']
            port = item['port']
            address = item['address']
            isanonymous = item['isanonymous']
            types = item['types']
            livetime = item['livetime']
            yanzhengtime = item['yanzhengtime']
            # print(country,ip,port,address,isanonymous,types,livetime,yanzhengtime)
            Xicidaili_mysql.insert_mysql(country,ip,port,address,isanonymous,types,livetime,yanzhengtime)
