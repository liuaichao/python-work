# -*- coding:utf-8 -*-
import pymysql
from 爬虫.Scrapy_xici.Scrapy_xici import settings
MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

conn = pymysql.connect(host=MYSQL_HOSTS, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB)
cursor = conn.cursor()
class Xicidaili_mysql(object):
    @classmethod
    def insert_mysql(cls,country,ip,port,address,isanonymous,types,livetime,yanzhengtime):

        sql = 'insert into xici_spider(country,ip,port,address,isanonymous,types,livetime,yanzhengtime) values(%(country)s,%(ip)s,%(port)s,%(address)s,%(isanonymous)s,%(types)s,%(livetime)s,%(yanzhengtime)s);'
        values = {
            'country':country,
            'ip':ip,
            'port':port,
            'address':address,
            'isanonymous':isanonymous,
            'types':types,
            'livetime':livetime,
            'yanzhengtime':yanzhengtime

        }

        try:
            cursor.execute(sql, values)
            # print(values)
            conn.commit()
        except:
            print('数据插入失败')
            conn.rollback()
