# -*- coding:utf-8 -*-
import tkinter
from mysql_demo import Mysql_demo
import tkinter.messagebox
class T_root_insrt():
    def __init__(self):
        pass
    def start(self):
        self.base = tkinter.Tk()
        self.base.geometry("300x400")
        self.base.geometry('+500+100')
        self.base.wm_title('书籍插入')

        self.lable1 = tkinter.Label(self.base, text='书 名', font=("微软雅黑", 18))
        self.lable1.place(x=0, y=10, width=70, height=50)
        self.entry1 = tkinter.Entry(self.base, font=("隶书", 22), width=20)
        self.entry1.place(x=70, y=15, width=220, height=40)

        self.lable2 = tkinter.Label(self.base, text='作 者', font=("微软雅黑", 18))
        self.lable2.place(x=0, y=60, width=70, height=50)
        self.entry2 = tkinter.Entry(self.base, font=("隶书", 22), width=20)
        self.entry2.place(x=70, y=65, width=220, height=40)

        self.lable3 = tkinter.Label(self.base, text='出版社', font=("微软雅黑", 18))
        self.lable3.place(x=0, y=110, width=70, height=50)
        self.entry3 = tkinter.Entry(self.base, font=("隶书", 22), width=20)
        self.entry3.place(x=70, y=115, width=220, height=40)
        # 提示
        self.lable4 = tkinter.Label(self.base, text='简 介', font=("微软雅黑", 18))
        self.lable4.place(x=0, y=160, width=70, height=50)
        self.entry4 = tkinter.Entry(self.base, font=("隶书", 22), width=20)
        self.entry4.place(x=70, y=165, width=220, height=40)

        self.lable5 = tkinter.Label(self.base, text='地 址', font=("微软雅黑", 18))
        self.lable5.place(x=0, y=210, width=70, height=50)
        self.entry5 = tkinter.Entry(self.base, font=("隶书", 22), width=20)
        self.entry5.place(x=70, y=215, width=220, height=40)

        self.lable6 = tkinter.Label(self.base, text='类 型', font=("微软雅黑", 18))
        self.lable6.place(x=0, y=255, width=70, height=50)
        self.entry6 = tkinter.Entry(self.base, font=("隶书", 22), width=20)
        self.entry6.place(x=70, y=265, width=220, height=40)
        #插入按钮
        self.Button1 = tkinter.Button(self.base, text="插 入", font=("隶书", 18), bg='cyan',command=self.button_1)
        self.Button1.place(x=100,y=350)

        self.base.mainloop()
    #插入响应按钮
    def button_1(self):
        my = Mysql_demo()
        sql = 'insert into book(title,author,publisher,recolagu,href,drop_type) values ("{0}","{1}","{2}","{3}","{4}","{5}");'.format(self.entry1.get(),self.entry2.get(),self.entry3.get(),self.entry4.get(),self.entry5.get(),self.entry6.get())
        my.insert(sql)
        hnt = tkinter.messagebox.showinfo('提示', '{0} 插入成功'.format(self.entry1.get()))



if __name__ == '__main__':
    a = T_root_insrt()
    a.start()