# -*- coding:utf-8 -*-
from pymongo import MongoClient
class MongoAPI(object):
    def __init__(self,table_name):
        self.db_ip = '192.168.0.200'
        self.db_port = 27017
        self.db_name = 'book_photo'
        self.table_name = table_name
        self.conn = MongoClient(host=self.db_ip, port=self.db_port)
        self.db = self.conn[self.db_name]
        self.table = self.db[self.table_name]
    #获取一条数据
    def get_one(self, query):
        return self.table.find_one(query, property={'_id':False})
    #获取多条数据
    def get_all(self, query):
        return self.table.find(query)
    #添加数据
    def add(self, query):
        return self.table.insert(query)
    #删除数据
    def delete(self, query):
        return self.table.delete_many(query)
    #更新数据
    def updata(self, query, kv_divt):
        return self.table.update_one(query, {'$set':kv_divt}, update=True)