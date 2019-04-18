# -*- coding:utf-8 -*-

'''
https://music.163.com/discover/artist/cat?id=1001
https://music.163.com/discover/artist/cat?id=1001&initial=65

'''
import requests
from lxml import etree
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def geshou(url):
    headers = {
        'User - Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Referer':'https://music.163.com/'
    }
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    driver.switch_to_frame("g_iframe")
    time.sleep(3)
    page_src = driver.page_source
    # print(page_src)
    html = etree.HTML(page_src)
    sin = html.xpath('//ul[@class="m-cvrlst m-cvrlst-5 f-cb"]/li/p/a[@class="nm nm-icn f-thide s-fc0"]')
    for i in sin:
        print(i.text)
    driver.quit()



if __name__ == '__main__':
    base_url = 'https://music.163.com/discover/artist/cat?'
    id = ['1001', '1002', '1003','2001', '2001', '2003', '6001', '6002', '6003','7001','7002','7003','4001','4002','4003']
    initial = [-1,65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 0]
    for i in id:
        for j in initial:
            url = base_url+'id='+str(i)+'&'+'initial='+str(j)
            # print(url)
            geshou(url)