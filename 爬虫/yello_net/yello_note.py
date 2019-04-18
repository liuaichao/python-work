# -*- coding:utf-8 -*-
import requests
from lxml import etree

headers = {
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
urls = [
       'https://www.723zh.com/novel/list5/']
list_num = 5
url_ss = []
for url in urls:
    req = requests.get(url, headers = headers)
    r = req.text
    b = r.encode('ISO-8859-1').decode(req.apparent_encoding)
    html = etree.HTML(b)
    yeshu = html.xpath('//span')[-1].text
    # print(yeshu)
    # xayi1 = html.xpath('//li/a[@class="disabled"]/@href')[1]
    yeshu = yeshu.split('/')[-1]
    for s in range(int(yeshu)+1):
        if s == 0:
            url_ss.append('https://www.723zh.com/novel/list'+str(list_num)+'/index.html')
        else:
            #https://www.723zh.com/novel/list2/index_2.html
            url_ss.append(str('https://www.787zh.com' + '/novel'+'/list'+str(list_num)+'/index' + str('_') + str(s) + str('.html')))
    list_num = int(list_num) + 1
# print(url_ss)
for url_s in url_ss:
    req = requests.get(url_s, headers = headers)
    r = req.text
    b = r.encode('ISO-8859-1').decode(req.apparent_encoding)
    html = etree.HTML(b)
    note_names = html.xpath('//div[@class="layout-box clearfix"]/ul/li/a/@title')
    note_urls = html.xpath('//div[@class="layout-box clearfix"]/ul/li/a/@href')
    for note_name,note_url in zip(note_names,note_urls):
            note_url = 'https://www.723zh.com'+str(note_url)
            req = requests.get(note_url, headers)
            r = req.text
            b = r.encode('ISO-8859-1').decode(req.apparent_encoding)
            htmls = etree.HTML(b)
            wenzi = htmls.xpath('//div[@class="xs-details-content text-xs"]//p/text()')
            print(note_name)
            for x in wenzi:
                with open('D:\python程序\爬虫\yello_net\小说\\'+note_name+'.txt','a', encoding='utf-8') as f:
                    f.write(str(x))


