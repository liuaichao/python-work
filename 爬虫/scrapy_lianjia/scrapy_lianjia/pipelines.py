# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from 爬虫.scrapy_lianjia.scrapy_lianjia import settings
import pymysql
from 爬虫.scrapy_lianjia.scrapy_lianjia.items import ScrapylianjiaItem
class ScrapyLianjiaPipeline(object):
    def process_item(self, item, spider):
        return item
class scrapyLianjiaPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host=settings.MYSQL_HOSTS,user=settings.MYSQL_USER,passwd=settings.MYSQL_PASSWORD,port=
                               settings.MYSQL_PORT, db=settings.MYSQL_DB)
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        self.sql = 'insert into lianjia_spider(name,price,url,search_name) values (%(name)s,%(price)s,%(url)s,%(search_name)s);'
        self.value = {
            'name':item['name'],
            'price':item['price'],
            'url':item['url'],
            'search_name':item['search_name']
        }
        try:
            self.cursor.execute(self.sql, self.value)
            self.conn.commit()
        except:
            self.conn.rollback()
            print('数据插入失败')

        return item