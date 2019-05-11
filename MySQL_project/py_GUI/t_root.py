# -*- coding:utf-8 -*-
#管理员登陆界面
import tkinter
from mysql_demo import Mysql_demo
from t_root_insert import T_root_insrt
from t_root_user import T_root_user
from book_list import Book
from t_root_bor import T_root_bor
from t_root_dian import T_root_dian
from t_root_ty import T_root_ty
from t_root_book_num import T_root_book_num
class T_root():
    def __init__(self):
        pass
    def start(self):
        self.base = tkinter.Tk()
        self.base.geometry("300x400")
        self.base.geometry('+400+100')
        self.base.wm_title('管理员')
        #按钮
        self.Button1 = tkinter.Button(self.base, text="   插 入 书 籍  ", font=("隶书", 18), bg='cyan',command=self.insert_book)
        self.Button1.pack()
        self.Button2 = tkinter.Button(self.base, text="   用 户 管 理  ", font=("隶书", 18), bg='cyan',command=self.user_g)
        self.Button2.pack()
        self.Button3 = tkinter.Button(self.base, text="   借 阅 表 单  ", font=("隶书", 18), bg='cyan',command=self.bor_book)
        self.Button3.pack()
        self.Button4 = tkinter.Button(self.base, text="点开数据分析分析", font=("隶书", 18), bg='cyan',command=self.diankai_book)
        self.Button4.pack()
        self.Button5 = tkinter.Button(self.base, text="点开种类数据分析", font=("隶书", 18), bg='cyan',command=self.bor_num)
        self.Button5.pack()
        self.Button6 = tkinter.Button(self.base, text="书籍借用数据分析", font=("隶书", 18), bg='cyan',command=self.use_book)
        self.Button6.pack()
        self.base.mainloop()
    #插入书籍
    def insert_book(self):
        a = T_root_insrt()
        a.start()

    #用户信息
    def user_g(self):
        a = T_root_user()
        a.start()

    #借书表
    def bor_book(self):
        a = T_root_bor()
        a.start()

    #点开
    def diankai_book(self):
        a = T_root_dian()
        a.start()

    #类型关注度
    def bor_num(self):
        a = T_root_ty()
        a.start()
    #书籍借用
    def use_book(self):
        a = T_root_book_num()
        a.start()


if __name__ == '__main__':
    a = T_root()
    a.start()