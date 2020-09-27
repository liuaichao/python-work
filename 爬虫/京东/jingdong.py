# -*- coding:utf-8 -*-
import requests
import json
import csv
import time
#构造url
url1 = ['https://sclub.jd.com/comment/productPageComments.action?'
        'callback=fetchJSON_comment98vv1909&productId=10557697913&score=0'
        '&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'.format(i) for i in range(30)]
url2 = ['https://sclub.jd.com/comment/productPageComments.action?'
        'callback=fetchJSON_comment98vv4550&productId=3423766&score=0'
        '&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1'.format(i) for i in range(30)]
url3 = ['https://sclub.jd.com/comment/productPageComments.action?'
        'callback=fetchJSON_comment98vv5674&productId=4232651&'
        'score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1'.format(i) for i in range(30)]
urls = url1+url2+url3
#构建csv
with open('content.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(['ID', '已采', '已发', '电商平台', '品牌', '评论', '时间', '型号', 'PageUrl'])
#构建头部信息
headers = {
    'Referer':'https://item.jd.com/10557697913.html',
    'Sec-Fetch-Mode': 'no-cors',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
#id
ID = 0
# [1,2,3]
# ['a','b','c']
# [(1,'a'),(2,'b')]
for url,i in zip(urls, range(90)):
    time.sleep(1)
    req = requests.get(url, headers=headers)
    # print(req.status_code)
    data = req.text[26:-2]
    # print(data)
    # print(len(data))
    # print(data)
    data = json.loads(data)
    #已采
    yicai = 'TURE'
    #已发
    yifa = 'FALSE'
    #电商平台
    pingtai = '京东'
    #品牌
    if i<30:
        pinpai = 'AO'
    elif i>=30 & i<60:
        pinpai = '美的'
    else:
        pinpai = '海尔'
    for j in range(10):
        ID = ID+1
        #评论
        pinglun = data['comments'][j]['content'].strip()
        #时间
        Time = '#######'
        #型号
        xinghao = data['comments'][j]['referenceName']
        #PageUrl
        pageurl = url
        #将数据整合在一起
        rows = [ID, yicai, yifa, pingtai, pinpai, pinglun, Time, xinghao, pageurl]
        # print(rows)
        #写入csv表格
        try:
            with open('./content.csv', 'a', newline='') as f:
                f_csv = csv.writer(f)
                f_csv.writerow(rows)
        except Exception as ex:
            print(ex)
            pass