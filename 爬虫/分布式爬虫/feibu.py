# -*- coding:utf-8 -*-
import requests
import redis
from lxml import etree
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Firedox/64.0.3282.186 Safari/537.36'
}
def push_redis_list():
    r = redis.Redis(host='192.168.0.200',port=6379)
    print(r.keys('*'))
    list_urls = []
    with open('D:\\pythonproject\\爬虫\\test\\url.txt','r') as f:
        file_list = f.readlines()
        for link in file_list:
            link = link.split(r'\n')[0].strip()
            list_urls.append(link)
    for url in list_urls:
        try:
            print('正在插入文字')
            if url != '':
                r.lpush('wenzi',url)
        except:
            continue
        print('现在文字链接的个数为',r.llen('wenzi'))
    return
def get_text():
    r = redis.Redis(host='192.168.0.200', port=6379)
    while True:
        try:
            url = r.lpop('wenzi')
            # url = url.decode('acsii')
            try:
                req = requests.get(url, headers=headers, timeout=20)
                html = req.text
                html = etree.HTML(html)
                content = html.xpath('//div[@class="entry"]//text()')
                title = html.xpath('//h1[@class="arti_title"]/text()')[0]
                string = ''
                for i in content:
                    string1 = i.strip()
                    string = string + string1.replace('\n', '')
                with open(title+".txt",'w', encoding='utf-8') as f:
                    f.write(string)
                    print('已经获取',title)
            except Exception as e:
                print('爬取内容失败',e)
        except Exception as e:
            print('url获取失败',e)
            break
    return

if __name__=='__main__':
    this_machine = 'master'
    if this_machine=='master':
        # push_redis_list()
        get_text()
    else:
        get_text()
