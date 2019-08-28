# -*- coding:utf-8 -*-
import requests
from UserAgent_demo import UserAgent
import random
import re
from lxml import etree

a = UserAgent()
headers = {
    'User-Agent':random.choice(a.getuseragent())
}


#https://movie.douban.com/subject/25823277/comments?start=20&limit=20&sort=new_score&status=P
#数据url
urls = ['https://movie.douban.com/subject/25823277/comments?start={0}&limit=20&sort=new_score&status=P'.format(i*20) for i in range(10)]
# print(urls)

for url in urls:
    req = requests.get(url,headers=headers)
    html = etree.HTML(req.text)
    data_comment = html.xpath('//div[@class="comment"]/p/span/text()')
    data_xing = html.xpath('//span[@class="comment-info"]/span[2]/@class')
    data_star = []
    for data_x in data_xing:
        data_j = re.findall(r'allstar(\d)0 rating',data_x)
        if data_j == []:
            data_j = ['0']
        data_star = data_star+data_j
    data_name = ['三生三世十里桃花']*20
    # print(data_name)
    #数据写入
    for i in range(len(data_comment)):
        with open('./data.txt', 'a+', encoding='utf_8_sig', newline='') as f:
            f.write(data_name[i]+'##')
            f.write(data_star[i]+'##')
            f.write(data_comment[i])
            f.write('\n')
