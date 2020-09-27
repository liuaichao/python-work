import requests
from UserAgent_demo import UserAgent
import random
import time
import re
from lxml import etree
a = UserAgent()

headers = {
    'User-Agent':random.choice(a.getuseragent())}
urls = ['https://item.jd.com/2830894.html'.format(i*20) for i in range(10)]
for url in urls:
    req = requests.get(url,headers=headers)
    html = etree.HTML(req.text)
    data_comment = html.xpath('//li[contains(@class,"gl-item")]')
    data_xing = html.xpath('div/div[@class="p-price"]/strong/csv()')
    data_star = []
    for data_x in data_xing:
        data_j = re.findall(r'allstar(\d)0 rating',data_x)
        if data_j == []:
            data_j = ['0']
        data_star = data_star+data_j
    data_name = ['万家乐']*20
    for i in range(len(data_comment)):
        with open('./data.csv', 'a+', encoding='utf_8_sig', newline='') as f:
            f.write(data_name[i]+'##')
            f.write(data_comment[i])
            f.write('\n')
