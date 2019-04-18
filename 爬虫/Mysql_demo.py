# -*- coding:utf-8 -*-
import pymysql

class Mysql_demo(object):
    #数据库连接
    def __init__(self, host, user, passwd, db):
        try:
            self.conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=3306)
            self.cursor = self.conn.cursor()
        except:
            print("MySQL数据库连接失败!")
    #数据库查询操作,传入sql语句
    def search(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            data = self.cursor.fetchall()
            return data
        except:
            self.conn.rollback()
            return False
    #数据库插入操作
    def insert(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
    #数据库


