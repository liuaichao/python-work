# -*- coding:utf-8 -*-
import tkinter
import t_user
from t_register import T_register
from mysql_demo import Mysql_demo
from book_list import Book
from book_det import Book_det
from termcolor import *
from book_det import Book_det
from t_return import Return_book
from t_root import T_root
class MN():
    def __init__(self):
        self.book = Book()
        pass
    def start(self):
        self.base = tkinter.Tk()
        self.base.geometry("800x500")
        self.base.geometry('+200+100')
        self.base.wm_title('网络图书管理系统')
        # 提示按钮
        self.lable = tkinter.Label(self.base, text='   请登录：         ', font=("微软雅黑", 18))
        self.lable.place(x=0, y=0, width=150, height=50)
        # 登录按钮
        self.Button_submit = tkinter.Button(self.base, text="登录", font=("隶书", 18), bg='blue', command=self.t_submit)
        self.Button_submit.place(x=200, y=10, width=50, height=30)
        # 注册按钮
        self.Button_register = tkinter.Button(self.base, text="注册", font=("隶书", 18), command=self.register)
        self.Button_register.place(x=300, y=10, width=50, height=30)
        # 分割线
        self.fengexian1 = tkinter.Label(self.base, text='——————————————————————————————————————————————————', font=("微软雅黑", 18))
        self.fengexian1.place(x=0, y=40, width=1000, height=10)
        # 搜索框
        self.var_entry = tkinter.Variable()
        self.entry = tkinter.Entry(self.base, font=("隶书", 22), width=20,textvariable=self.var_entry)
        self.entry.place(x=100, y=50, width=500, height=40)
        # 搜索按钮
        self.Button_search = tkinter.Button(self.base, text="搜索", font=("隶书", 18), bg='cyan',command=self.search)
        self.Button_search.place(x=620, y=50)
        # 列表
        self.var = tkinter.StringVar()
        global lb
        self.lb = tkinter.Listbox(self.base, listvariable=self.var,font=("隶书", 12))
        self.list_item = [i for i in range(1,31)]
        for item in self.list_item:
            self.lb.insert(tkinter.END, item)

        #设置list的值
        self.var.set((self.book.first_book_list()))
        self.lb.bind('<ButtonRelease-1>', self.print_item)
        self.scrl = tkinter.Scrollbar(self.base)
        self.scrl.place(x=600, y=100, height=340)
        self.lb.configure(yscrollcommand=self.scrl.set)
        self.lb.place(x=20, y=100, width=580, height=340)
        self.scrl['command'] = self.lb.yview

        #类型列表
        self.vars = tkinter.StringVar()
        self.lbs = tkinter.Listbox(self.base, listvariable=self.vars, font=("隶书", 12))
        self.list_items = [i for i in range(1, 223)]
        for item in self.list_items:
            self.lbs.insert(tkinter.END, item)
        # 设置list的值
        self.vars.set((('0-2岁', '3-6岁', '一般管理学', '世界名著', '世界政治', '世界文化', '世界美食', '两性关系', '个人理财', '中医保健', '中国儿童文学', '中国古代哲学', '中国古代随笔', '中国古典小说', '中国古诗词', '中国当代小说', '中国政治', '中国文化', '中国民族音乐', '中国现当代诗歌', '中国现当代随笔', '中国经济', '中国近现代小说', '中小学教辅', '中老年', '书画', '人体艺术', '人工智能', '人生哲学', '人际交往', '企业软件开发与实施', '会计', '传统文化', '传记', '体育明星', '作品集', '作品集/作品赏析', '作曲/指挥', '侦探/悬疑/推理', '保健/心理健康', '保健食谱营养', '保险', '信息安全', '健康百科', '健身', '其他国外青春文学', '军事', '农业/林业', '初中通用', '动漫/卡通', '励志/成长', '医学', '历代帝王', '历史人物', '历史知识读物', '历史读物', '叛逆/成长', '口才/演讲/辩论', '古代家具', '古籍整理', '史学理论', '史料典籍', '史类', '吉它', '名人励志', '后期处理', '哲学', '哲学知识读物', '四大名著', '国内自助旅游指南', '国外自助旅游指南', '国画', '国际法', '国际经济', '地图/地理', '地域文化', '地方史志', '城市自助旅游指南', '声乐', '外交、国际关系', '外国儿童文学', '外国小说', '外国诗歌', '外国随笔', '外国音乐', '外语', '大学英语', '子部', '孕产妇/育儿', '孕产百科', '字帖', '学者', '宗教', '宝石', '家居/休闲游戏', '家常食谱', '家庭与办公室用书', '家庭教育', '寓言传说', '小说', '少儿英语', '工业技术', '工具书', '工艺美术', '市场/营销', '常见病', '建筑', '建筑艺术', '影视制作', '影视明星', '影视理论', '影视赏析', '征订教材', '心灵与修养', '心理健康', '心理学', '性格与习惯', '悬疑/惊悚', '戏剧', '成功/励志', '成功/激励', '技法/教程', '技法教程', '拓展读物', '摄影器材', '摄影理论', '操作系统/系统开发', '收藏百科', '收藏随笔', '政治', '政治人物', '教师用书', '教育', '数据库', '数码摄影', '文化理论', '文化评述', '文学', '文学家', '文学理论', '文集', '新闻传播出版', '旅游', '旅游摄影/画册', '旅游攻略', '旅游随笔', '校园', '民俗文化', '民族史志', '民间艺术', '水粉水彩', '油画', '法律', '法律法规', '法的理论', '港台青春文学', '爆笑/无厘头', '玄幻/新武侠/魔幻/科幻', '玉器', '理论', '理论/欣赏', '生活常识', '电子商务', '电脑杂志――合订本', '益智游戏', '研究生/本科/专科教材', '硬笔书法', '碑帖', '社会学', '社会科学', '神秘现象', '科学家', '科幻', '科普/百科', '科普读物', '程序设计', '童话', '篆刻', '素描速写', '经济法', '经济理论', '经济通俗读物', '经部', '绘画理论', '美丽装扮', '美学', '美食', '考古文物', '考试', '育儿百科', '自传', '自然科学', '舞台艺术戏曲', '艺术家', '艺术理论', '艺术类考试', '艺术课堂', '英语考试', '英语读物', '行业/职业英语', '计算机体系结构', '计算机教材', '计算机理论', '计算机考试认证', '认知', '设计', '语文阅读', '语言文字', '软件工程/开发项目管理', '通俗音乐', '金融/投资', '钢琴', '钱币', '陶瓷', '集部', '雕品', '雕塑', '青春文学', '餐饮指南', '饮食文化', '高中通用', '高考')))
        self.lbs.bind('<ButtonRelease-1>', self.type_item)
        self.scrls = tkinter.Scrollbar(self.base)
        self.scrls.place(x=775, y=100, height=340)
        self.lbs.configure(yscrollcommand=self.scrls.set)
        self.lbs.place(x=630, y=100,height=340)
        self.scrls['command'] = self.lbs.yview
        self.base.mainloop()


    # 事件绑定
    def print_item(self,event):
        # try:
            self.book_name = (self.lb.get(self.lb.curselection())).split('       ')[0]
            #根据book_name查找
            self.my_s = Mysql_demo()
            self.sql_s = 'select title,author,publisher,recolagu,href,drop_type from book where title="{0}";'.format(self.book_name)
            self.book_data = self.my_s.search(self.sql_s)
            self.bde = Book_det(self.id, self.name,self.book_name,self.book_data[0][5])
            self.bde.start(self.book_data)

        # except:
        #     submit_warn = tkinter.messagebox.showinfo('警告', '请先登录！')
    #类型点击响应方法
    def type_item(self,event):
        self.type_name = self.lbs.get(self.lbs.curselection())
        # print(self.type_name)
        a = Book()
        self.var.set(a.type_book_list(self.type_name))



    # 登录
    def submit(self):
        s = t_user.T_submit()
        s.t_submit()



    # 注册
    def register(self):
        r = T_register()
        r.register()
    #搜索
    def search(self):
        self.entry_con = self.var_entry.get()
        self.entry_con = list(self.entry_con)
        self.sql_re = '.*'
        for i in self.entry_con:
            self.sql_re = self.sql_re+i+'.*'
        self.sql_s = Mysql_demo()
        self.sql_search = "select title,author from book where title regexp '({0})';".format(self.sql_re)
        self.search_datas = self.sql_s.search(self.sql_search)
        # print(self.search_datas)
        #判断返回值
        if self.search_datas != False:
            #清空列表
            self.lb.delete(0,tkinter.END)
            self.list_item = [i for i in range(len(self.search_datas))]
            for item in self.list_item:
                self.lb.insert(tkinter.END, item)
            #添加list数据
            data_list = []
            for i in self.list_item:
                data_list.append(self.search_datas[i][0]+'       '+self.search_datas[0][1])
            data_list = tuple(data_list)
            self.var.set((data_list))
            self.lb.bind('<ButtonRelease-1>', self.print_item)
        else:
            # 清空列表
            self.lb.delete(0, tkinter.END)

    def t_submit(self):
        self.bases = tkinter.Tk()
        self.bases.geometry("300x400")
        self.bases.geometry('+500+100')
        self.bases.wm_title('登录')
        # 提示
        self.lable1 = tkinter.Label(self.bases, text='电 话', font=("微软雅黑", 18))
        self.lable1.place(x=0, y=10, width=70, height=50)
        # 手机号输入框
        self.entry1 = tkinter.Entry(self.bases, font=("隶书", 22), width=20)
        self.entry1.place(x=70, y=15, width=220, height=40)
        # 提示
        self.lable2 = tkinter.Label(self.bases, text='密 码', font=("微软雅黑", 18))
        self.lable2.place(x=0, y=65, width=70, height=50)
        # 密码输入框
        self.entry2 = tkinter.Entry(self.bases, font=("隶书", 22), width=20, show="*")
        self.entry2.place(x=70, y=65, width=220, height=40)
        # 登录按钮
        self.Button1 = tkinter.Button(self.bases, text="登录", font=("隶书", 18), bg='cyan', command=self.t_is_submit)
        self.Button1.place(x=50, y=140, width=200)
        # 用户登录按钮
        self.Button2 = tkinter.Button(self.bases, text="用户登录", font=("隶书", 10), state=tkinter.DISABLED)
        self.Button2.place(x=30, y=350, width=55)
        # 学生登录按钮
        self.Button3 = tkinter.Button(self.bases, text="学生登录", font=("隶书", 10), command=self.t_std_submit)
        self.Button3.place(x=200, y=350, width=55)
        self.bases.mainloop()

    # 学生登陆
    def t_std_submit(self):
        self.lable1.destroy()
        self.lable2.destroy()
        # 提示
        self.lable1 = tkinter.Label(self.bases, text='学 号', font=("微软雅黑", 18))
        self.lable1.place(x=0, y=10, width=70, height=50)
        # 提示
        self.lable2 = tkinter.Label(self.bases, text='密 码', font=("微软雅黑", 18))
        self.lable2.place(x=0, y=65, width=70, height=50)
        self.Button2['state'] = tkinter.NORMAL
        self.Button3['state'] = tkinter.DISABLED
        self.Button2['command'] = self.t_submit

    # 登录按钮函数
    def t_is_submit(self):

        self.id = self.entry1.get()
        self.pwd = self.entry2.get()
        if self.id == 'root' and self.pwd=='123456':
            a = T_root()
            a.start()
        else:
            self.to_mysql()

    # 数据库查询
    def to_mysql(self):
        if self.id == '' or self.pwd == '':
            self.hnt = tkinter.messagebox.showerror('错误', '请输入账号密码')
        else:
            self.my = Mysql_demo()
            self.sql = 'select name from user where id="{0}" and pwd="{1}";'.format(self.id, self.pwd)
            self.name = self.my.search(self.sql)
            if self.name != False:
                self.hnt = tkinter.messagebox.showinfo('提示', '登录成功,欢迎,{0}'.format(self.name[0][0]))
                self.bases.destroy()
                #登录后变化
                self.lable.destroy()
                self.Button_submit.destroy()
                self.Button_register.destroy()
                self.lable = tkinter.Label(self.base, text='欢迎，{0}'.format(self.name[0][0]), font=("微软雅黑", 18))
                self.lable_title = tkinter.Label(self.base,text='Welcome Book World',font=("微软雅黑", 18),fg='orange')
                self.Button_per = tkinter.Button(self.base, text="退出登录", font=("隶书", 18), bg='cyan',command=self.person)
                self.Button_per.place(x=550,y=0)
                self.Button_huan = tkinter.Button(self.base, text="还书系统", font=("隶书", 18), bg='lawngreen',command=self.return_boo)
                self.Button_huan.place(x=680, y=0)
                self.lable_title.place(x=0,y=0)
                self.lable.place(x=300, y=0, width=200, height=40)


            else:
                self.hnt = tkinter.messagebox.showerror('错误', '账号或密码出错了')
    #个人中心
    def person(self):
        self.lable.destroy()
        self.Button_per.destroy()
        self.Button_huan.destroy()
        self.lable_title.destroy()
        self.lable = tkinter.Label(self.base, text='   请登录：         ', font=("微软雅黑", 18))
        self.lable.place(x=0, y=0, width=150, height=50)
        # 登录按钮
        self.Button_submit = tkinter.Button(self.base, text="登录", font=("隶书", 18), bg='blue', command=self.t_submit)
        self.Button_submit.place(x=200, y=10, width=50, height=30)
        # 注册按钮
        self.Button_register = tkinter.Button(self.base, text="注册", font=("隶书", 18), command=self.register)
        self.Button_register.place(x=300, y=10, width=50, height=30)
        self.fengexian1 = tkinter.Label(self.base, text='——————————————————————————————————————————————————',
                                        font=("微软雅黑", 18))
        self.fengexian1.place(x=0, y=40, width=1000, height=10)

    #还书系统
    def return_boo(self):
        self.re_book = Return_book(self.id)
        self.re_book.start()

    # def after_submit(self):
    #
    #     self.lable.destroy()
    #     self.Button_submit.destroy()
    #     self.Button_register.destroy()
    #     self.lable = tkinter.Label(self.base, text='欢迎，{0}'.format(self.name[0][0]), font=("微软雅黑", 18))
    #     self.lable.place(x=200, y=0, width=200, height=50)

if __name__ == '__main__':
    user_acount = ''
    user_name = ''
    lb = ''
    a = MN()
    a.start()


