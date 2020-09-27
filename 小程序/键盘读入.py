# -*- coding:utf-8 -*-
#键盘读入以ctrl+d结束
import sys
D = sys.stdin.read()
space=0
t=0
H=0
for i in D:
    if i==' ':
        space=space+1
    elif i=='\t':
        t=t+1
    elif i=='\n':
        H=H+1
print('{} {} {}'.format(space,t,H))




