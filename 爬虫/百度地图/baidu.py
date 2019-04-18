# -*- coding:utf-8 -*-
import requests
import json
import time
import pymysql
from 爬虫.Mysql_demo import Mysql_demo
headers = {
    'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
}
def get_data(citys):
    page = 0
    key = 1
    for city in citys:
        # print(city)
        while True:
            url = 'http://api.map.baidu.com/place/v2/search?' \
                  'query={0}&region={1}&output=json&page_size=20&' \
                  'page_num={2}&ak=mx0XTZftMf30RpvGzfbSv4UGiu4u5bP6'.format('公园',city , str(page))
            print(url)
            time.sleep(1)
            req = requests.get(url, headers=headers)
            # print(req.text)
            data = json.loads(req.text)
            # print(data)
            if data['results']==[]:
                page = 0
                break
            else:
                page = int(page)+1

            results = data['results']
            for result in results:
                name = result['name']
                province = result['province']
                city = result['city']
                area = result['area']
                address = result['address']
                uid = result['uid']
                # print(name+' '+province+city+area+' '+address+' '+uid)
                data_to_mysql(key,name, province, city, area, address, uid)
                key = key+1

def get_info():
    my = Mysql_demo('192.168.0.200','root','lac981215lac','spider')
    uids = my.search('select uid from baidu_map')
    key = 1
    for uid in uids:
        # print(uid[0])
        url = 'http://api.map.baidu.com/place/v2/detail?uid={0}&output=json&scope=2&ak=mx0XTZftMf30RpvGzfbSv4UGiu4u5bP6'.format(uid[0])
        req = requests.get(url, headers=headers)
        data = json.loads(req.text)
        try:
            name = data['result']['name']
        except:
            name = None
        try:
            city = data['result']['city']
        except:
            city = None
        try:
            address = data['result']['address']
        except:
            address = None
        try:
            tel = data['result']['telephone']
        except:
            tel = None
        try:
            detail_url = data['result']['detail_info']['detail_url']
        except:
            detail_url = None
        try:
            shop_hours = data['result']['detail_info']['shop_hours']
        except:
            shop_hours = None
        try:
            content_tag = data['result']['detail_info']['content_tag']
        except:
            content_tag = None

        # print(name, city, address, tel, detail_url, shop_hours, content_tag)
        sql = "insert into baidumap_info values({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(key,name, city, address, tel, detail_url, shop_hours,content_tag)
        print(sql)
        my.insert(sql)
        key = key+1



def data_to_mysql(key,name, province, city, area, address, uid):
    db = pymysql.connect(host='192.168.0.200',user='root',passwd='lac981215lac',db='spider',port=3306)
    cursor = db.cursor()
    sql = "insert into baidu_map values({0},'{1}','{2}','{3}','{4}','{5}','{6}')".format(key,name, province, city, area, address, uid)

    try:
        cursor.execute(sql)
        db.commit()
        # print(name, province, city, area, address, uid)
    except:
        db.rollback()

if __name__ == '__main__':
    url = 'http://api.map.baidu.com/place/v2/search?query=%E5%85%AC%E5%9B%AD&region=%E5%B1%B1%E4%B8%9C%E7%9C%81&output=json&page_size=20&page_num=0&ak=mx0XTZftMf30RpvGzfbSv4UGiu4u5bP6'
    time.sleep(1)
    req = requests.get(url)
    js = json.loads(req.text)
    js = js['results']
    citys = []
    for i in js:
        citys.append(i['name'])
    # get_data(citys)
    get_info()
    # print(citys)
