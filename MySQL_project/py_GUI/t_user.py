# -*- coding:utf-8 -*-
import tkinter
from 数据抓取.mysql_demo import Mysql_demo
import tkinter.messagebox
import t_main
class T_submit():
    #登录窗口，默认用户登录
    def __init__(self):
        self.base = tkinter.Tk()
        self.base.geometry("300x400")
        self.base.geometry('+500+100')
        self.base.wm_title('登录')
    def t_submit(self):

        #提示
        self.lable1 = tkinter.Label(self.base, text='电 话', font=("微软雅黑", 18))
        self.lable1.place(x=0, y=10, width=70, height=50)
        # 手机号输入框
        self.entry1 = tkinter.Entry(self.base, font=("隶书", 22), width=20)
        self.entry1.place(x=70, y=15, width=220, height=40)
        #提示
        self.lable2 = tkinter.Label(self.base, text='密 码', font=("微软雅黑", 18))
        self.lable2.place(x=0, y=65, width=70, height=50)
        # 密码输入框
        self.entry2 = tkinter.Entry(self.base, font=("隶书", 22), width=20,show = "*")
        self.entry2.place(x=70, y=65, width=220, height=40)
        #登录按钮
        self.Button1 = tkinter.Button(self.base, text="登录", font=("隶书", 18), bg='cyan', command=self.t_is_submit)
        self.Button1.place(x=50, y=140,width=200)
        #用户登录按钮
        self.Button2 = tkinter.Button(self.base, text="用户登录", font=("隶书", 10),	state=tkinter.DISABLED)
        self.Button2.place(x=30, y=350,width=55)
        # 学生登录按钮
        self.Button3 = tkinter.Button(self.base, text="学生登录", font=("隶书", 10),command=self.t_std_submit)
        self.Button3.place(x=200, y=350, width=55)
        self.base.mainloop()
    #学生登陆
    def t_std_submit(self):
        self.lable1.destroy()
        self.lable2.destroy()
        # 提示
        self.lable1 = tkinter.Label(self.base, text='学 号', font=("微软雅黑", 18))
        self.lable1.place(x=0, y=10, width=70, height=50)
        # 提示
        self.lable2 = tkinter.Label(self.base, text='密 码', font=("微软雅黑", 18))
        self.lable2.place(x=0, y=65, width=70, height=50)
        self.Button2['state'] = tkinter.NORMAL
        self.Button3['state'] = tkinter.DISABLED
        self.Button2['command'] = self.t_submit
    #登录按钮函数
    def t_is_submit(self):

        self.id = self.entry1.get()
        self.pwd = self.entry2.get()
        self.to_mysql()
    #数据库查询
    def to_mysql(self):
        if self.id == ''or self.pwd == '':
            self.hnt = tkinter.messagebox.showerror('错误', '请输入账号密码')
        else:
            self.my = Mysql_demo()
            self.sql = 'select name from user where id="{0}" and pwd="{1}";'.format(self.id, self.pwd)
            self.name = self.my.search(self.sql)
            if self.name != False:
                self.hnt = tkinter.messagebox.showinfo('提示', '登录成功,欢迎,{0}'.format(self.name[0][0]))
                self.base.destroy()
                # self.after_submit()

            else:
                self.hnt = tkinter.messagebox.showerror('错误','账号或密码出错了')
    #登陆后主界面发生改变
    # def after_submit(self):
    #     self.after_submit(self.name)



if __name__ == '__main__':
    a = T_submit()
    a.t_submit()

