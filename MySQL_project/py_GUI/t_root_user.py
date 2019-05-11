# -*- coding:utf-8 -*-
import tkinter
from book_list import Book
from mysql_demo import Mysql_demo
class T_root_user():
    def __init__(self):
        pass
    def start(self):
        self.base = tkinter.Tk()
        self.base.geometry("300x400")
        self.base.geometry('+500+100')
        self.base.wm_title('用户管理')
        #列表
        self.var = tkinter.StringVar()
        self.lb = tkinter.Listbox(self.base, listvariable=self.var, font=("隶书", 12))
        self.book = Book()
        for item in self.book.root_user():
            self.lb.insert(tkinter.END, item)
        # 设置list的值
        self.lb.bind('<ButtonRelease-1>', self.print_item)
        self.scrl = tkinter.Scrollbar(self.base)
        self.scrl.place(x=270, y=10, height=340)
        self.lb.configure(yscrollcommand=self.scrl.set)
        self.lb.place(x=20, y=10, width=250, height=340)
        self.scrl['command'] = self.lb.yview
        self.base.mainloop()

    #列表点击事件
    def print_item(self,event):
        pass
    def my_sql(self):
        self.b = Mysql_demo()
        self.sql = 'select id from user'
        self.data = self.b.search(self.sql)
        return len(self.data)

if __name__ == '__main__':
    a = T_root_user()
    a.start()
