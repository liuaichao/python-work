# -*- coding:utf-8 -*-
import pymysql
db = pymysql.connect(host='47.105.142.252',user='anonymous',passwd='lac981215lac',db='test',port=3306)
# cursor = db.cursor()
# cursor.execute('create table py_test(name varchar (4),age int(3))')
print(db)