# -*- coding:utf-8 -*-
import requests
from urllib import request
import time
from selenium import webdriver
import socket

def Schedule(blocknum, blocksize, totalsize):
    per = 100*blocknum*blocksize/totalsize
    print("当前下载进度为:{0}".format(per))

url = 'https://d2.xia12345.com/down/109/2018/11/jhkua53m.mp4'
# req = requests.get(url)
request.urlretrieve(url, 'D:\yello\\' + 'rq' + '.mp4', Schedule)