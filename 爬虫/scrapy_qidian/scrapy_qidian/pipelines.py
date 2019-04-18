# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from 爬虫.scrapy_qidian.scrapy_qidian import settings
class ScrapyQidianPipeline(object):
    def process_item(self, item, spider):
        return item


class scrapyQidianPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host=settings.MYSQL_HOSTS, user=settings.MYSQL_USER, passwd=settings.MYSQL_PASSWORD, db=settings.MYSQL_DB, port=settings.MYSQL_PORT)
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        sql = 'insert into qidian_spider(title,info,author,refer) values (%(title)s,%(info)s,%(author)s,%(refer)s);'

        values = {
            'title':item['title'],
            'info':item['info'],
            'author':item['author'],
            'refer':item['refer']
        }
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
        except:
            print('数据插入失败')
            self.conn.rollback()

        return item