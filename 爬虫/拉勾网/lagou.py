# -*- coding:utf-8 -*-

import requests
from lxml import etree
from UserAgent_demo import UserAgent
import random
from selenium import webdriver
import time
#https://www.lagou.com/zhaopin/Java/?filterOption=3
#https://www.lagou.com/zhaopin/Java/2/?filterOption=3
#https://www.lagou.com/zhaopin/Java/3/?filterOption=3
#https://www.lagou.com/zhaopin/C++/?filterOption=3
#https://www.lagou.com/zhaopin/C++/2/?filterOption=3
user_agent = UserAgent()
url_java = ['https://www.lagou.com/zhaopin/Java/{0}/?filterOption=3'.format(i) for i in range(1,31)]
url_cpp = ['https://www.lagou.com/zhaopin/C++/{0}/?filterOption=3'.format(i) for i in range(1,31)]
#要爬取的地址列表
urls = url_java+url_cpp
#初始化
driver = webdriver.Chrome()
#登录
driver.get('https://www.lagou.com/zhaopin/Java/?labelWords=label')
time.sleep(25)
for url in urls:
    # headers = {
    #     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #     'Accept-Encoding':'gzip, deflate, br',
    #     'Host':'www.lagou.com',
    #     'Cookie':'_ga=GA1.2.2139487507.1551785625; user_trace_token=20190305193343-883d7ef5-3f3a-11e9-9535-525400f775ce; LGUID=20190305193343-883d8341-3f3a-11e9-9535-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1557982837; LGSID=20190516130037-8b88c8ea-7797-11e9-a01d-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0tbFB0FNkUsKkeVkT00000ZBec7C00000Im9PLT.THL0oUhY1x60UWYLrj0YnjDvn7t1P7qsusK15H-bnWb1nAFBnj0snHn4PH00IHY0mHdL5iuVmv-b5HnznWTznHbYnHnhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8UA7MULR8mvqVQvk9UhwGUhTVTA7Muiqsmzq1uy7zmv68pZwVUjqdIAdxTvqdThP-5ydxmvuxmLKYgvF9pywdgLKWmMf0mLFW5HDvP1f4%26tpl%3Dtpl_11534_19713_15764%26l%3D1512094584%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591-%252520%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3227219413_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D7%26ie%3Dutf-8%26f%3D8%26ch%3D13%26tn%3D78040160_34_pg%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26oq%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rqlang%3Dcn; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; LG_HAS_LOGIN=1; _putrc=9C56E6CA4776F258123F89F2B170EADC; JSESSIONID=ABAAABAABEEAAJA381BE9DA152C5A095E6D26F56F7DFE3C; login=true; hasDeliver=0; gate_login_token=eea6b7363d2d65b3f4c0d3ba5da32cb63fc30757bddfad5fbc5c3e624c1645d5; _gid=GA1.2.934457977.1557982897; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_navigation; SEARCH_ID=3fde30cd22cd40499c9aa86259441a4b; X_HTTP_TOKEN=a0842b118efa788185148975517dc8aab273c7cc9f; _gat=1; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B74961; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1557984168; LGRID=20190516132249-a543b9df-779a-11e9-9acd-525400f775ce',
    #     'Upgrade-Insecure-Requests':'1',
    #     'User-Agent':random.choice(user_agent.getuseragent())
    # }
    # req = requests.get(url,headers=headers)
    # print(url)
    # print(req.text)
    #等待时间
    time.sleep(random.choice([0.7,1,1.2,1.3,1.5,1.7,2,2.1]))
    driver.get(url)
    page_data = driver.page_source
    html = etree.HTML(page_data)
    #标题
    title = html.xpath('//div[@class="p_top"]/a/h3/text()')
    #地址
    addr = html.xpath('//div[@class="p_top"]/a/span/em/text()')
    #介绍
    cont = html.xpath('//div[@class="li_b_r"]/text()')
    print(title)
    print(addr)
    print(cont)
    print('-----------------------')

driver.quit()
