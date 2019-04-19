import requests
from lxml import etree
#http://www.qlu.edu.cn/38/list2.htm
# urls = []
# for i in range(1000):
#     url = 'http://www.qlu.edu.cn/38/list{0}.htm'.format(str(i+1))
#     urls.append(url)
# # print(urls)
# for url in urls:
#     req = requests.get(url)
#     html = req.text
#     html = etree.HTML(html)
#     hrefs = html.xpath('//ul/li/span/a/@href')[:-1:]
#     for href in hrefs:
#         if href[0]=='/':
#             href = 'http://www.qlu.edu.cn'+href
#             with open('url.txt','a') as f:
#                 f.write(href)
#                 f.write('\n')
#         else:
#             pass
        # print(href)
url = 'http://www.qlu.edu.cn/2019/0417/c38a124389/page.htm'
req = requests.get(url)
html = req.text
html = etree.HTML(html)
content = html.xpath('//div[@class="entry"]//text()')
title = html.xpath('//h1[@class="arti_title"]/text()')[0]
string = ''
for i in content:
    string1 = i.strip()
    string = string+string1.replace('\n','')

print(title)