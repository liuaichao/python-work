# -*- coding:utf-8 -*-
import tkinter
from mysql_demo import Mysql_demo
class Return_book():
    def __init__(self,count):
        self.acount = count
    def start(self):
        self.base = tkinter.Tk()
        self.base.geometry("500x500")
        self.base.geometry('+500+100')
        self.base.wm_title('还书中心')
        #标题
        self.label1 = tkinter.Label(self.base, text='已借书', font=("微软雅黑", 18))
        self.label1.place(x=100,y=0,width=200)
        #数据库查询已借书目
        self.my = Mysql_demo()
        sql = 'select count(*) from bor_book where acount="{0}"'.format(self.acount)
        num = self.my.search(sql)[0][0]

        if num==0:
            pass
        elif num==1:
            self.book_1()
        elif num==2:
            self.book_2()
        elif num==3:
            self.book_3()
        self.base.mainloop()
    #1本
    def book_1(self):
        sql = 'select book_name,r_date from bor_book where acount="{0}"'.format(self.acount)
        self.datas = self.my.search(sql)

        self.label2 = tkinter.Label(self.base, text=self.datas[0][0], font=("微软雅黑", 15))
        self.label2.place(x=0,y=70,width=300)
        self.label3 = tkinter.Label(self.base, text=self.datas[0][1], font=("微软雅黑", 15))
        self.label3.place(x=320, y=70, width=180)
        self.button_1 = tkinter.Button(self.base, text="归还", font=("隶书", 18), bg='cyan',command=self.button1)
        self.button_1.place(x=400,y=120)
    # 2本
    def book_2(self):
        sql = 'select book_name,r_date from bor_book where acount="{0}"'.format(self.acount)
        self.datas = self.my.search(sql)
        self.label2 = tkinter.Label(self.base, text=self.datas[0][0], font=("微软雅黑", 15))
        self.label2.place(x=0, y=40, width=300)
        self.label3 = tkinter.Label(self.base, text=self.datas[0][1], font=("微软雅黑", 15))
        self.label3.place(x=320, y=40, width=180)
        self.button_1 = tkinter.Button(self.base, text="归还", font=("隶书", 18), bg='cyan',command=self.button1)
        self.button_1.place(x=400, y=90)
        #2
        self.label3 = tkinter.Label(self.base, text=self.datas[1][0], font=("微软雅黑", 15))
        self.label3.place(x=0, y=150, width=300)
        self.label4 = tkinter.Label(self.base, text=self.datas[1][1], font=("微软雅黑", 15))
        self.label4.place(x=320, y=150, width=180)
        self.button_2 = tkinter.Button(self.base, text="归还", font=("隶书", 18), bg='cyan',command=self.button2)
        self.button_2.place(x=400, y=200)

    # 3本
    def book_3(self):
        sql = 'select book_name,r_date from bor_book where acount="{0}"'.format(self.acount)
        self.datas = self.my.search(sql)
        self.label2 = tkinter.Label(self.base, text=self.datas[0][0], font=("微软雅黑", 15))
        self.label2.place(x=0, y=40, width=300)
        self.label3 = tkinter.Label(self.base, text=self.datas[0][1], font=("微软雅黑", 15))
        self.label3.place(x=320, y=40, width=180)
        self.button_1 = tkinter.Button(self.base, text="归还", font=("隶书", 18), bg='cyan',command=self.button1)
        self.button_1.place(x=400, y=90)
        # 2
        self.label3 = tkinter.Label(self.base, text=self.datas[1][0], font=("微软雅黑", 15))
        self.label3.place(x=0, y=150, width=300)
        self.label4 = tkinter.Label(self.base, text=self.datas[1][1], font=("微软雅黑", 15))
        self.label4.place(x=320, y=150, width=180)
        self.button_2 = tkinter.Button(self.base, text="归还", font=("隶书", 18), bg='cyan',command=self.button2)
        self.button_2.place(x=400, y=200)
        #3
        self.label5 = tkinter.Label(self.base, text=self.datas[2][0], font=("微软雅黑", 15))
        self.label5.place(x=0, y=260, width=300)
        self.label6 = tkinter.Label(self.base, text=self.datas[2][1], font=("微软雅黑", 15))
        self.label6.place(x=320, y=260, width=180)
        self.button_3 = tkinter.Button(self.base, text="归还", font=("隶书", 18), bg='cyan',command=self.button3)
        self.button_3.place(x=400, y=310)
    #按钮的事件响应
    def button1(self):
        self.my_s = Mysql_demo()
        sql = 'delete from bor_book where acount="{0}" and book_name="{1}";'.format(self.acount,self.datas[0][0])
        self.my_s.delete(sql)
        sql = 'update user set borrow=borrow+1 where id="{0}";'.format(self.acount)
        self.my_s.update(sql)
        self.button_1['text'] = '已归还'
        self.button_1['state'] = tkinter.DISABLED
        self.button_1['bg'] = 'lightyellow'
    def button2(self):
        self.my_s = Mysql_demo()
        sql = 'delete from bor_book where acount="{0}" and book_name="{1}";'.format(self.acount, self.datas[1][0])
        self.my_s.delete(sql)
        sql = 'update user set borrow=borrow+1 where id="{0}";'.format(self.acount)
        self.my_s.update(sql)
        self.button_2['text'] = '已归还'
        self.button_2['state'] = tkinter.DISABLED
        self.button_2['bg'] = 'lightyellow'

    def button3(self):
        self.my_s = Mysql_demo()
        sql = 'delete from bor_book where acount="{0}" and book_name="{1}";'.format(self.acount, self.datas[2][0])
        self.my_s.delete(sql)
        sql = 'update user set borrow=borrow+1 where id="{0}";'.format(self.acount)
        self.my_s.update(sql)
        self.button_3['text'] = '已归还'
        self.button_3['state'] = tkinter.DISABLED
        self.button_3['bg'] = 'lightyellow'
if __name__ == '__main__':
    a = Return_book('201703040038')
    a.start()