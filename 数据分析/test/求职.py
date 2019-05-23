#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author zzk
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
driver = webdriver.Chrome()

def parse_link():
    # url = 'https://www.lagou.com/'
    # driver.get(url)
    # resp = driver.page_source
    # soup = BeautifulSoup(resp,'lxml')
    # all_positions = soup.select('div.menu_sub.dn  dl  dd  a')
    # joburls = [i['href'] for i in all_positions]
    # for joburl in (joburls):
    driver.get('https://www.lagou.com/zhaopin/Java/?labelWords=label')
    time.sleep(20)
    for page in range(1, 31):
            link = ('https://www.lagou.com/zhaopin/Java/'+str(page)+'/?filterOption='+ str(page))
            time.sleep(2)
            driver.get(link)
            resp = driver.page_source
            soup =BeautifulSoup(resp,'lxml')
            positions = soup.select('a.position_link h3')
            adds = soup.select('ul  li  div.list_item_top  div.position  div.p_top  a  span  em')
            publishs = soup.select('span.format-time ')
            moneys = soup.select('ul  li  div.list_item_top  div.position  div.p_bot  div  span')
            needs = soup.select('ul  li  div.list_item_top  div.position  div.p_bot  div')
            companys = soup.select('ul  li  div.list_item_top  div.company  div.company_name  a')
            tags = []
            if soup.find('div', class_='li_b_l'):
                tags = soup.select('ul  li  div.list_item_bot  div.li_b_l')
            fulis = soup.select('ul  li  div.list_item_bot  div.li_b_r')
            for position,add,publish,money,need,company,tag,fuli in zip(positions,adds,publishs,moneys,needs,companys,tags,fulis):
                data_a = [
                    '岗位信息：' + position.get_text(),
                    '工作地址：' + add.get_text(),
                    '发布时间：' + publish.get_text(),
                    '薪资信息：' + money.get_text(),
                    '工作需求：' + need.get_text().split('\n')[2],
                    '发布公司：' + company.get_text(),
                    '招聘信息标签：' + tag.get_text().replace('\n','-'),
                    '公司福利：' + fuli.get_text()
                        ]
                print(data_a)
    return driver
if __name__ == '__main__':
    a = parse_link()
    a.quit()