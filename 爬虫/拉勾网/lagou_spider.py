#!/usr/bin/env python
#author zzk
#!/usr/bin/env python
# author zzk
from bs4 import BeautifulSoup
import time
import urllib.request
import urllib.parse
import pymysql
import io
import random
import sys
import urllib.error

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


def spider_a():

            url = 'https://www.lagou.com/'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400',
                'Cookie': 'io = ce3170bc-705c-49b1-aa74-77fea8fff031;user_trace_token = 20190806073104-c840556d-24b7-4999-a465-296cad794b24; _ga = GA1.2.2125842603.1565047866; LGUID = 20190806073105-1821eae9-b7d9-11e9-a4fb-5254005c3644; index_location_city =%E5%85%A8%E5%9B%BD; X_HTTP_TOKEN = 733e029cfe00f0062621145651a03f7599c266f0fc; _gid = GA1.2.806164946.1565411263; _gat = 1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6 = 1565047866, 1565411263; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6 = 1565411263; LGSID = 20190810122742-31ef69cc-bb27-11e9-88ea-525400f775ce; PRE_UTM =; PRE_HOST =; PRE_SITE =; PRE_LAND = https%3A%2F%2Fwww.lagou.com%2F; LGRID = 20190810122742 - 31ef6ba7 - bb27 - 11e9 - 88ea - 525400f775ce; sm_auth_id = 9d1o49qbbippjq38',
                # 'Host':'sm.lagou.com',
                'Connection': 'keep - alive',
                'Content - Length': '16',
                # 'Accept': '* / *',
                # 'Referer': 'https: // www.lagou.com /',

            }
            request = urllib.request.Request(url =url,headers=headers)
            response = urllib.request.urlopen(request)
            soup = BeautifulSoup(response,'lxml')
            all_informations = soup.select('div.menu_sub.dn  dl  dd  a')
            job_urls = [i['href'] for i in all_informations]
            print(job_urls)
            for job_url in job_urls:
                for page in range(1, 31):
                        print(page)
                        link = '{}{}/?filterOption=3'.format(job_url, str(page))
                        if False:
                            pass
                        request_a = urllib.request.Request(url =link,headers=headers)
                        time.sleep(random.uniform(0, 0.05))
                        try:
                            resp = urllib.request.urlopen(request_a)
                        except urllib.error.URLError as e:
                            print(e)
                            soup =BeautifulSoup(resp,'lxml')
                            informations = soup.select('a.position_link h3')
                            publishers = soup.select('span.format-time ')
                            adds = soup.select('ul  li  div.list_item_top  div.position  div.p_top  a  span  em')
                            moneys = soup.select('ul  li  div.list_item_top  div.position  div.p_bot  div  span')
                            needs = soup.select('ul  li  div.list_item_top  div.position  div.p_bot  div')
                            companys = soup.select('ul  li  div.list_item_top  div.company  div.company_name  a')
                            tags = []
                            if soup.find('div', class_='li_b_l'):
                                tags = soup.select('ul  li  div.list_item_bot  div.li_b_l')
                            fulis = soup.select('ul  li  div.list_item_bot  div.li_b_r')
                            for information,publish,add,money,need,company,tag,fuli in zip(informations,adds,publishers,moneys,needs,companys,tags,fulis):
                                    岗位信息=information.get_text()
                                    工作地址=publish.get_text()
                                    发布时间=add.get_text()
                                    薪资信息=money.get_text()
                                    经验要求=need.get_text().split('\n')[2]
                                    发布公司=company.get_text()
                                    招聘信息=tag.get_text().replace('\n','-')
                                    公司福利=fuli.get_text()
                                    print(岗位信息)
                                    # db = pymysql.connect('localhost', 'root', '123456', 'dashuju')
                                    # print('ok')
                                    # cursor = db.cursor()
                                    # sql = "INSERT INTO `dashuju`.`lagou` (`岗位信息`, `工作地址`, `发布时间`, `薪资信息`, `经验要求`, `发布公司`, `招聘信息`, `公司福利`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (岗位信息,工作地址,发布时间,薪资信息,经验要求,发布公司,招聘信息,公司福利)
                                    #
                                    # cursor.execute(sql)
                                    # db.commit()





if __name__ == '__main__':
    spider_a()  #爬虫
