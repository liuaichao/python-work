# -*- coding:utf-8 -*-
from mysql_demo import Mysql_demo
import random
class Book():
    #首页列表返回
    def first_book_list(self):
        datas = list()
        self.rand_num = [random.randint(830,100000) for _ in range(0,30)]
        a = Mysql_demo()
        for i in self.rand_num:
            self.sql = 'select title,author from book where _id={0};'.format(i)
            data = a.search(self.sql)
            datas.append(data[0][0]+'       '+data[0][1])
        datas = tuple(datas)
        return datas
    #首页类型返回
    def type_book_list(self,type_name):
        datas = list()
        a = Mysql_demo()
        sql = 'select title,author from book where drop_type="{0}";'.format(type_name)
        data = a.search(sql)
        for i in range(len(data)):
            datas.append(data[i][0]+'       '+data[i][1])
        datas = tuple(datas)
        return datas
    #管理员的用户管理返回
    def root_user(self):
        datas = list()
        a = Mysql_demo()
        sql = 'select id,borrow from user;'
        data = a.search(sql)
        for i in range(len(data)):
            datas.append(data[i][0]+'    '+str(data[i][1]))
        datas = tuple(datas)
        return datas
    #管理员借阅表
    def root_bor(self):
        datas = list()
        a = Mysql_demo()
        sql = 'select acount,b_date,book_name from bor_book;'
        data = a.search(sql)
        for i in range(len(data)):
            datas.append(data[i][0] + ' '+data[i][1]+' ' + str(data[i][2]))
        datas = tuple(datas)
        return datas

if __name__ == '__main__':
    a = Book()
    print(a.root_bor())