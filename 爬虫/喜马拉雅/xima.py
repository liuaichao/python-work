# -*- coding:utf-8 -*-
import re
import requests
from urllib import request
from pypinyin import lazy_pinyin
import time
import json
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
'''
https://www.ximalaya.com/revision/play/album?albumId=3595841&pageNum=1&sort=-1&pageSize=30
'''
headers = {
    'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Referer': 'https://music.163.com/'
}
def url_leixing(type):
    base_url = 'https://www.ximalaya.com/yinyue/'
    type_url = base_url+type+'/'
    print(type_url)
    return type_url
def music_url(type_url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(type_url)
    html = driver.page_source
    # print(driver.page_source)
    albumids = re.findall(r'"albumId":(\d*)',html)
    ht = etree.HTML(html)
    titles = ht.xpath('//span[@class="v-m _5NW5"]/text()')
    # print(titles)
    driver.quit()
    url_all = []
    for albumid in albumids:
        url = 'https://www.ximalaya.com/revision/play/album?albumId={}&pageNum=1&sort=-1&pageSize=30'.format(str(albumid))
        # print(url)
        url_all.append(url)
    return url_all
def get_download_url(url_all):
    for url in url_all:
        print(url)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        html = driver.page_source
        html = html.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">', '')
        html = html.replace('</pre></body></html>','')
        # print(html)
        html = json.loads(html)
        for i in html['data']['tracksAudioPlay']:
            url_download = i['src']
            name = i['trackName']
            music_download(url_download, name)
            # print(name)

        driver.quit()
        time.sleep(1)
def music_download(url_download, name):
    if '/' in name:
        name = name.replace('/', '-')
    if ' | ' in name:
        name = name.replace(' | ', '-')
    request.urlretrieve(url_download, 'D:\python程序\爬虫\喜马拉雅\音乐\\'+name+'.mp3')

if __name__ == '__main__':
    type = input("请输入要下载的音乐类型:")
    type = ''.join(lazy_pinyin(type))
    # print(type)
    a = url_leixing(type)
    url_all = music_url(a)
    get_download_url(url_all)
    # print(url_all)
