# -*- coding:utf-8 -*-
import tkinter
import random
import time

#英雄机
class plane1():
    #px代表图像的锚点,height代表图像的高度
    def __init__(self, px, py, height, width):
        self.px = px
        self.py = py
        self.height = height
        self.width = width
        #定义英雄的图像
        self.imgpy1 = tkinter.PhotoImage(file="../img/飞机1.gif")

    #英雄移动
    def pl1_move(self, position):
        a = position
        if a == "38":
            self.py -=1
        elif a == '37':
            self.px -=1
        elif a == "40":
            self.py +=1
        elif a == "39":
            self.px +=1




root_window = tkinter.Tk()
root_window.resizable(width=False, height=False)
root_window.title('飞机大战')
# 创建画布
window_canvas = tkinter.Canvas(root_window, width=480, height=600)
window_canvas.pack()


def ap_move():
    window_canvas.move("bg", m.px, m.py)

    print(m.px,m.py)
    window_canvas.after(1000, ap_move)

#实例化plane1
m = plane1(240,300,30,30)
window_canvas.create_image(m.px, m.py, anchor=tkinter.CENTER, image=m.imgpy1, tags='bg')
root_window.bind('<Key-Left>', m.pl1_move('37'))
root_window.bind('<Key-Right>', m.pl1_move('39'))
ap_move()
root_window.mainloop()


root_window.mainloop()

