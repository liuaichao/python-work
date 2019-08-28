# -*- coding:utf-8 -*-
import requests
from lxml import etree
import UserAgent_demo
import random

urls = [('http://www.cnmo.com/reviews/danping/{0}/').format(i) for i in range(1,38)]

for url in urls:
    print(url)
    user_agent = UserAgent_demo.UserAgent()
    a = user_agent.getuseragent()
    headers = {
        'User-Agent':random.choice(a)
    }
    try:
        req = requests.get(url,headers=headers,timeout=5)
    except Exception as ex:
        print(ex)
    html = etree.HTML(req.text)
    data = html.xpath('//a[@class="tag"]')
    no = 1
    for i in data:
        if no%2==0:
            print(i.text.strip())
        no += 1

