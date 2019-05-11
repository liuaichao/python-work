# -*- coding:utf-8 -*-
import tkinter
from mysql_demo import Mysql_demo
import tkinter.messagebox
class T_register():
    def __init__(self):
        self.base = tkinter.Tk()
        self.base.geometry("300x400")
        self.base.geometry('+500+100')
        self.base.wm_title('注册')
        self.gender = ''
    def register(self):
        # 提示
        self.lable1 = tkinter.Label(self.base, text='电 话', font=("微软雅黑", 18))
        self.lable1.place(x=0, y=10, width=70, height=50)
        # 手机号输入框
        self.entry1 = tkinter.Entry(self.base, font=("隶书", 22), width=20)
        self.entry1.place(x=70, y=15, width=220, height=40)
        # 提示
        self.lable2 = tkinter.Label(self.base, text='密 码', font=("微软雅黑", 18))
        self.lable2.place(x=0, y=65, width=70, height=50)
        # 密码输入框
        self.entry2 = tkinter.Entry(self.base, font=("隶书", 22), width=20, show="*")
        self.entry2.place(x=70, y=65, width=220, height=40)
        # 提示
        self.lable3 = tkinter.Label(self.base, text='姓 名', font=("微软雅黑", 18))
        self.lable3.place(x=0, y=110, width=70, height=50)
        #姓名输入框
        self.entry3 = tkinter.Entry(self.base, font=("隶书", 22), width=20)
        self.entry3.place(x=70, y=115, width=220, height=40)
        # 提示
        self.lable4 = tkinter.Label(self.base, text='性 别', font=("微软雅黑", 18))
        self.lable4.place(x=0, y=155, width=70, height=50)
        #单选框
        self.r = tkinter.IntVar()
        self.radio1 = tkinter.Radiobutton(self.base, text="男",variable=self.r, value='男', font=("微软雅黑", 15), command=self.nan)
        self.radio1.place(x=100,y=160)
        self.radio2 = tkinter.Radiobutton(self.base, text="女", variable=self.r,value='女', font=("微软雅黑", 15),command=self.nv)
        self.radio2.place(x=160,y=160)
        #注册按钮
        self.Button1 = tkinter.Button(self.base, text="注册", font=("隶书", 18), bg='cyan', command=self.reg)
        self.Button1.place(x=50, y=250,width=200)
        #用户注册按钮
        self.Button2 = tkinter.Button(self.base, text="用户注册", font=("隶书", 10),	state=tkinter.DISABLED)
        self.Button2.place(x=30, y=350,width=55)
        # 学生注册按钮
        self.Button3 = tkinter.Button(self.base, text="学生注册", font=("隶书", 10), command=self.t_std_reg)
        self.Button3.place(x=200, y=350, width=55)

        self.base.mainloop()
    def nan(self):
        self.gender = self.radio1['value']

    def nv(self):
        self.gender = self.radio2['value']

    #学生注册
    def t_std_reg(self):
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
        self.Button2['command'] = self.register
    #注册
    def reg(self):
        # print(self.gender)
        self.tel = self.entry1.get()
        self.pwd = self.entry2.get()
        self.name = self.entry3.get()
        self.gender = self.gender
        # print(self.tel,self.pwd,self.name,self.gender)
        self.to_mysql()
    def to_mysql(self):
        self.my = Mysql_demo()
        self.sql = 'insert into user values ("{0}","{1}","{2}","{3}","{4}")'.format(self.tel,self.pwd,self.name,self.gender,3)
        self.my.insert(self.sql)
        #提示框
        self.hnt = tkinter.messagebox.showinfo('提示', '注册成功,前往登录')
        self.base.destroy()

if __name__ == '__main__':
    a = T_register()
    a.register()
