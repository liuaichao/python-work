# -*- coding:utf-8 -*-
import tkinter
import requests
from lxml import etree
import os
from PIL import Image, ImageTk
import time
from tkinter import scrolledtext
import pymysql
import datetime
from mysql_demo import Mysql_demo
class Book_det():
    def __init__(self,acount,name,book_name,drop_type):
        self.acount = acount
        self.name = name[0][0]
        self.book_name = book_name
        a = Mysql_demo()
        sql = 'insert into book_dian(book_name,drop_type) values ("{0}","{1}")'.format(self.book_name,drop_type)
        a.insert(sql)
    def start(self,book_name):
        self.base = tkinter.Toplevel()
        self.base.geometry("600x400")
        self.base.geometry('+500+100')
        self.base.wm_title(book_name[0][0])
        self.bor_name = book_name[0][0]
        #书名
        self.lable1 = tkinter.Label(self.base, text='书名: '+book_name[0][0], font=("微软雅黑", 15),anchor='w')
        self.lable1.place(x=270, y=40,width=300)
        #作者
        self.lable2 = tkinter.Label(self.base, text='作者: '+book_name[0][1], font=("微软雅黑", 15),anchor='w')
        self.lable2.place(x=270, y=80,width=300)
        #出版社
        self.lable3 = tkinter.Label(self.base, text='出版社: '+book_name[0][2], font=("微软雅黑", 15),anchor='w')
        self.lable3.place(x=270, y=120,width=300)
        #概述
        # self.lable4 = tkinter.Label(self.base, text='概述: ' + book_name[0][3], font=("微软雅黑", 15),wraplength=300,justify='left',anchor='n')
        # self.lable4.place(x=270, y=120, width=300,height=190)
        # self.scrl = tkinter.Scrollbar(self.base)
        # self.scrl.place(x=570,y=120,height=190)

        self.scrl_text = scrolledtext.ScrolledText(self.base, width=30, height=150, wrap=tkinter.WORD,font=("微软雅黑", 12))
        self.scrl_text.insert(tkinter.END,'概述: '+book_name[0][3])
        self.scrl_text.place(x=270,y=150,height=150)
        # self.lable4.configure(yscrollcommand=self.scrl.set)
        # self.scrl['command'] = self.lable4.yview
        #图片
        self.headers = {
            'Referer': 'http://www.bookschina.com/',
            'Host': 'www.bookschina.com',
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        }
        req = requests.get(book_name[0][4],headers=self.headers)
        html = etree.HTML(req.text)
        self.photo_url = html.xpath('//a[@class="img"]/img/@src')[0]
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        }

        with open('D:\\pythonproject\\MySQL_project\\book_photo\\'+book_name[0][0]+'.png','wb') as f:
            res = requests.get(self.photo_url,headers=self.headers)
            f.write(res.content)
        img = Image.open("D:\\pythonproject\\MySQL_project\\book_photo\\"+book_name[0][0]+'.png')  # 打开图片
        self.book_photo = ImageTk.PhotoImage(img)
        self.lable4 = tkinter.Label(self.base,image = self.book_photo)
        self.lable4.place(x=10, y=30, width=212,height=300)
        #借阅按钮
        self.Button_bor = tkinter.Button(self.base, text="借阅", font=("隶书", 15), bg='cyan',command=self.borrow)
        self.Button_bor.place(x=330, y=330, width=150)
        self.base.mainloop()
    #借书
    def borrow(self):
        #查询是否还有借书条件
        self.my_is = Mysql_demo()
        sql = 'select borrow from user where id="{0}";'.format(self.acount)
        data = self.my_is.search(sql)[0][0]
        if data>0:
            #获取当前时间戳
            time1 = time.time()
            #获取20天后的时间戳
            time2 = time.time()+20*24*60*60
            time_b = time.strftime("%Y/%m/%d %H:%M",time.localtime(time1))
            time_r = time.strftime("%Y/%m/%d %H:%M", time.localtime(time2))
            self.my = Mysql_demo()
            sql = 'insert into bor_book values ("{0}","{1}","{2}","{3}","{4}");'.format(self.acount,self.name,time_b,time_r,self.bor_name)
            self.my.insert(sql)
            # 修改自己借书数目
            self.my_g = Mysql_demo()
            sql = 'update user set borrow={0} where id="{1}";'.format(data-1,self.acount)
            self.my_g.update(sql)
            self.hnn = tkinter.messagebox.showinfo('提示', '借书成功,请在{0}之前归还'.format(time_r))
            #修改书的剩余量
            my = Mysql_demo()
            sql = 'update book set re_qu=re_qu-1 where title={0};'.format(self.book_name)
            my.update(sql)
            self.base.destroy()
        else:
            self.hnt = tkinter.messagebox.showinfo('提示', '您借书已超过上限,无法再次借书！')
            self.base.destroy()

if __name__ == '__main__':
    a = Book_det()
    data = (('鲁滨逊漂流记sadsfasf','刘爱超','清华大学出版社','撒的看法和卡拉地方埃里克森符合几号放假啊的爱上福建安徽课件撒低级埃里克声嘶力竭的女生空间的','http://www.bookschina.com/7424433.htm'),)
    a.start(data)