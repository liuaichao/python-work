# -*- coding:utf-8 -*-
import requests
import UserAgent_demo
import random
from lxml import etree
import time
import csv
#请求每一页跟数据
def start(url, area):
    #构造头部信息
    user_agent = UserAgent_demo.UserAgent()
    a = user_agent.getuseragent()
    headers = {
        'User-Agent':random.choice(a)
    }

    urls = [(url+'pg{0}/').format(i) for i in range(1,71)]
    #每一页进行循环
    m = 0
    for url in urls:
        print(url)
        req = requests.get(url,headers=headers)
        html = etree.HTML(req.text)
        details_urls = html.xpath('//ul[@class="listContent"]/li/a/@href')
        #地区
        area = area
        #详情页循环
        # print(details_urls)

        for details_url in details_urls:
            try:
                de_req = requests.get(details_url,headers=headers, timeout=10)
                de_html = etree.HTML(de_req.text)
                # 户型
                huxing = de_html.xpath('//div[@class="base"]/div[@class="content"]/ul/li[1]/text()')
                huxing = huxing[0].strip()
                #楼层高度
                loucenggaodu = de_html.xpath('//div[@class="base"]/div[@class="content"]/ul/li[2]/text()')
                loucenggaodu = loucenggaodu[0].strip()
                #建筑面积
                jianzhumianji = de_html.xpath('//div[@class="base"]/div[@class="content"]/ul/li[3]/text()')
                jianzhumianji = jianzhumianji[0].strip().replace('㎡','')
                #建成年代
                jianchengniandai = de_html.xpath('//div[@class="base"]/div[@class="content"]/ul/li[8]/text()')
                jianchengniandai = jianchengniandai[0].strip()
                #装修情况
                zhuangxiuqingkuang = de_html.xpath('//div[@class="base"]/div[@class="content"]/ul/li[9]/text()')
                zhuangxiuqingkuang = zhuangxiuqingkuang[0].strip()
                #有无电梯
                youwudianti = de_html.xpath('//div[@class="base"]/div[@class="content"]/ul/li[14]/text()')
                youwudianti = youwudianti[0].strip()
                #挂牌价
                guapaijia = de_html.xpath('//div[@class="msg"]/span[1]/label/text()')
                guapaijia = guapaijia[0].strip()
                #成交周期
                chengjiaozhouqi = de_html.xpath('//div[@class="msg"]/span[2]/label/text()')
                chengjiaozhouqi = chengjiaozhouqi[0].strip()
                #调价次数
                tiaojiacishu = de_html.xpath('//div[@class="msg"]/span[3]/label/text()')
                tiaojiacishu = tiaojiacishu[0].strip()
                #带看次数
                daikancishu = de_html.xpath('//div[@class="msg"]/span[4]/label/text()')
                daikancishu = daikancishu[0].strip()
                # 关注人数
                guanzhurenshu = de_html.xpath('//div[@class="msg"]/span[5]/label/text()')
                guanzhurenshu = guanzhurenshu[0].strip()
                #浏览次数
                liulancishu = de_html.xpath('//div[@class="msg"]/span[6]/label/text()')
                liulancishu = liulancishu[0].strip()
                #成交价
                chengjiaojia = de_html.xpath('//span[@class="dealTotalPrice"]/i/text()')
                chengjiaojia = chengjiaojia[0].strip()
                data = [area,huxing,loucenggaodu,jianzhumianji,jianchengniandai,zhuangxiuqingkuang,
                        youwudianti,guapaijia,chengjiaozhouqi,tiaojiacishu,daikancishu,
                        guanzhurenshu,liulancishu,chengjiaojia]


                #文件逐行写如csv
                with open('./data_beijing.csv','a+',encoding='utf_8_sig',newline='') as f:
                    f_csv = csv.writer(f)
                    f_csv.writerow(data)
                print(data)

            except Exception as e:
                print(e)
                continue
#获取所有地区的url地址
def get_allurl():
    user_agent = UserAgent_demo.UserAgent()
    a = user_agent.getuseragent()
    headers = {
        'User-Agent': random.choice(a)
    }
    req = requests.get('https://bj.lianjia.com/chengjiao/',headers=headers)
    html = etree.HTML(req.text)
    urls = html.xpath('//div[@data-role="ershoufang"]/div[1]/a/@href')
    urls = ['https://bj.lianjia.com'+ url for url in urls]
    areas = html.xpath('//div[@data-role="ershoufang"]/div[1]/a/text()')
    areas = [area.strip() for area in areas]
    urls[17] = 'https://lf.lianjia.com/chengjiao/yanjiao/'
    urls[18] = 'https://lf.lianjia.com/chengjiao/xianghe/'
    print(urls)
    print(areas)
    # https: // bj.lianjia.com / chengjiao / dongcheng /
    for i in range(7,19):
        print('开始下载地区：'+areas[i])
        start(urls[i], areas[i])
        time.sleep(random.choice([1,1.5,2,2.5,3,3.5]))


if __name__=='__main__':
    #构建列名
    # with open('./data_beijing.csv', 'a+', encoding='utf_8_sig',newline='') as f:
    #     f_csv = csv.writer(f)
    #     f_csv.writerow(['地区','户型','楼层高度','建筑面积/㎡','建成年代/年','装修情况','有无电梯	','挂牌价/万','成交周期/天','调价次数/次'
    #                        ,'带看次数','关注人数','浏览次数','成交价/万'])
    get_allurl()