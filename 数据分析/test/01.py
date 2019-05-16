# -*- coding:utf-8 -*-
from MySQL_project.数据抓取.mysql_demo import Mysql_demo
my = Mysql_demo()

sql = 'select title from book'
data = my.search(sql)

with open(r'D:\pythonproject\数据分析\gensim\book_title.txt','w',encoding='utf-8') as f:
    for i in data:
        f.write(str(i[0]))
        f.write('\n')
