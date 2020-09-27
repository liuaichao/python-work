# -*- coding:utf-8 -*-
import six

import tkinter
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
from urllib import request
from selenium.webdriver.chrome.options import Options
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
def get_url():
    getname = entry.get()
    url = 'https://music.163.com/search/'
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    driver.switch_to_frame("g_iframe")
    # print(driver.page_source)
    driver.find_element_by_id('m-search-input').send_keys(getname)
    driver.find_element_by_id('m-search-input').send_keys(Keys.ENTER)
    # print(driver.current_url)
    url2 = driver.current_url + "&type=1"
    get_download(url2)
    # print(driver.page_source)
    driver.get(url2)
    driver.quit()
def get_download(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    driver.switch_to_frame("g_iframe")
    # print(driver.page_source)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    title = soup.select('.text')
    id = (re.findall(r'id=(\d*)"', str(title[0])))[0]
    music_name = title[0].get_text()
    singer_name = title[1].get_text()
    # print(id, music_name, singer_name)
    # cookie = driver.get_cookies()
    driver.quit()
    down_url = 'https://music.163.com/song/media/outer/url?id='+str(id)+'.mp3'
    down_load(down_url, music_name, singer_name)


def down_load(url, music_name, singer_name):
    # print(url)

    try:
        req = requests.get(url, headers=headers, allow_redirects=False)
        url = req.headers['Location']
        # print(url)
        request.urlretrieve(url, music_name[:10]+'.mp3')
        text.insert(1, music_name + '--' + singer_name + '   下载完成')
    except:
        text.insert(1, music_name + '--' + singer_name + '   下载失败！！')
if __name__ == '__main__':
    base = tkinter.Tk()
    base.geometry("800x500")
    base.geometry('+200+100')
    base.wm_title('网易云音乐下载')
    lable = tkinter.Label(base,text='请输入要下载的音乐：',font=("微软雅黑",22))
    lable.grid()
    entry = tkinter.Entry(base, font=("微软雅黑",22), width=30)
    entry.grid(row=0,column=1)
    text = tkinter.Listbox(base,font=('宋体',11),width=112,height=25)
    text.grid(row=1, columnspan=2)
    button_start = tkinter.Button(base,text="开始",font=("隶书",22),command=get_url)
    button_start.grid(row=2, column=0)
    button_quit = tkinter.Button(base,text="退出",font=("隶书",22),command=quit)
    button_quit.grid(row=2, column=1)
    base.mainloop()
