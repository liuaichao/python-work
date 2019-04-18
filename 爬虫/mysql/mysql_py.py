# -*- coding:utf-8 -*-
import pymysql
db = pymysql.connect(host='192.168.0.200',user='root',passwd='lac981215lac',db='spider',port=3306)
cursor = db.cursor()
cursor.execute('create table py_test(name varchar (4),age int(3))')
print(db)