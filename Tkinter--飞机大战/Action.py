# -*- coding:utf-8 -*-
import tkinter
import time
import configparser
# 加载现有配置文件
config = configparser.ConfigParser()
config.read('configparser.ini')
a = config.get(section='plane1', option='v1')
print(a)