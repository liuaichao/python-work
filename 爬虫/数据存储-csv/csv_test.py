# -*- coding:utf-8 -*-
import csv
import requests
from lxml import etree
url = "http://gaokao.xdf.cn/201812/10838473.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11;Ubuntu; Linux x86_64; rv:58.0) Geck0/20100101 Firedox/58.0',
}
req = requests.get(url, headers=headers)
req.encoding = 'utf-8'
# print(req.text)
html = etree.HTML(req.text)
rows = html.xpath('//tbody/tr/td')
rowss = rows[5:]
# print(len(rows))
# print("hhhhhhhhhhhhhhhhhhhhhhh")
list1 =[]
lists = []
a = 0
for row in rowss:
    #print(row.text.strip())
    if a<=4:
        list1.append(row.text.strip())
        a = a+1
    if a==5:
        a = 0
        list1 = tuple(list1)
        lists.append(list1)
        list(list1)
        list1 = []
# print(lists)
with open('test.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(lists)