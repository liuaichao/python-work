# -*- coding:utf-8 -*-
import tkinter
from mysql_demo import Mysql_demo
import json
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import scrolledtext
from PIL import Image, ImageTk
class T_root_ty():
    def __init__(self):
        # 数据分析跟数据可视化
        try:
            self.my = Mysql_demo()
            sql = 'select drop_type,count(*) from book_dian GROUP BY drop_type ORDER BY count(*) desc;'
            datas = self.my.search(sql)
            data1 = list()
            data2 = list()
            if len(datas) > 10:
                for i in range(10):
                    data1.append(datas[i][0])
                    data2.append(datas[i][1])
            else:
                for i in range(len(datas)):
                    data1.append(datas[i][0])
                    data2.append(datas[i][1])
            data = {"书名": data1, "数量": data2}
            data = json.dumps(data)
            student = pd.read_json(data)
            # print(student)
            student.plot.pie(x='书名',y='数量',labels=data1)
            plt.savefig('D:\\pythonproject\\MySQL_project\\data_a\\test1.jpg')
        except Exception as ex:
            print(ex)

    def start(self):
        self.base = tkinter.Toplevel()
        self.base.geometry("640x480")
        self.base.geometry('+500+100')
        self.base.wm_title('类型关注度')
        # 图片显示
        img = Image.open('D:\\pythonproject\\MySQL_project\\data_a\\test1.jpg')
        self.book_photo = ImageTk.PhotoImage(img)
        self.lable = tkinter.Label(self.base,image = self.book_photo)
        self.lable.pack()

        self.base.mainloop()

if __name__ == '__main__':
    a = T_root_ty()
    a.start()