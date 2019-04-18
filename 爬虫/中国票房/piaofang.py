# -*- coding:utf-8 -*-
import requests
from lxml import etree
import pandas as pd

url = 'http://www.cbooo.cn/year?year=2019'
req = requests.get(url).text
html = etree.HTML(req)
names = html.xpath('//tr/td/a/@title')
leixings = html.xpath('//td[2]/text()')
piaofangs = html.xpath('//td[3]/text()')
piaojias = html.xpath('//td[4]/text()')
rencis = html.xpath('//td[5]/text()')
diqus = html.xpath('//td[6]/text()')
times = html.xpath('//td[7]/text()')
df = pd.DataFrame({
    '电影名':names,
    '类型':leixings,
    '票房':piaofangs,
    '票价':piaojias,
    '人次':rencis,
    '地区':diqus,
    '上映时间':times
})
df.to_csv('piaofang.csv',encoding='utf-8')
