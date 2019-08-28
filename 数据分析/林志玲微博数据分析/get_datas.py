# -*- coding:utf-8 -*-
import requests
from lxml import etree
import UserAgent_demo
import random
import json
import time
import csv
#构造头部信息
user_agent = UserAgent_demo.UserAgent()
a = user_agent.getuseragent_phone()
headers = {
    'User-Agent':random.choice(a)
}
# urls = ['https://m.weibo.cn/api/statuses/repostTimeline?'
#                'id=4347741368557605&page={}'.format(i) for i in range(15136)]

def start(urls):
    for url in urls:
        time.sleep(random.choice([1,2,3,1.5,2.5]))
        print(url)
        try:
            req = requests.get(url, headers=headers,timeout=6)
            html = req.text.encode('utf-8')
            html = json.loads(html)
        # print(html)
        except Exception as ex:
            print(ex)
            time.sleep(10)
            try:
                # time.sleep(random.choice([5,7,9]))
                req = requests.get(url, headers=headers, timeout=6)
                html = req.text.encode('utf-8')
                html = json.loads(html)
            except:
                continue
        try:
            #ok
            ok = html['ok']
            #msg
            msg = html['msg']
            #data1概括
            data1 = html['data']['data'][0]
            #created_at
            created_at = data1['created_at']
            #id
            ids = data1['id']
            #mid
            mid = data1['mid']
            #can_edit
            can_edit = data1['can_edit']
            #raw_text
            raw_text = data1['raw_text']
            #source
            source = data1['source']
            #user概况
            user = data1['user']
            #user.description
            user_description = user['description']
            #user.follow_count
            user_follow_count = user['followers_count']
            #gender
            user_gender = user['gender']
            #user.id
            user_id = user['id']
            #user.mbrank
            user_mbrank = user['mbrank']
            #user.mbtype
            user_mbtype = user['mbtype']
            #user.profile_url
            user_profile_url = user['profile_url']
            #user.profile_image_url
            user_profile_image_url = user['profile_image_url']

            #retweeted_status.user概述
            retweeted = data1['retweeted_status']['user']
            # user.screen_name
            user_screen_name = retweeted['screen_name']
            #user.statuses_count
            user_statuses_count = retweeted['statuses_count']
            #user.urank
            user_urank = retweeted['urank']
            #user.verified
            user_verified = retweeted['verified']
            #user.verified_reason
            user_veridied_reason = retweeted['verified_reason']
            # print(ok,msg,created_at,ids,mid,can_edit,raw_text,source,user_description,
            #       user_follow_count,user_gender,user_id,user_mbrank,user_mbtype,user_profile_url,
            #       user_profile_image_url,user_screen_name,user_statuses_count,user_urank,user_verified,
            #       user_veridied_reason)

            data = [ok,msg,created_at,ids,mid,can_edit,raw_text,source,user_description,
                  user_follow_count,user_gender,user_id,user_mbrank,user_mbtype,user_profile_url,
                  user_profile_image_url,user_screen_name,user_statuses_count,user_urank,user_verified,
                  user_veridied_reason]
            # 文件逐行写如csv
            with open('./data.csv', 'a+', encoding='utf_8_sig', newline='') as f:
                f_csv = csv.writer(f)
                f_csv.writerow(data)
            print(data)
        except Exception as ex:
            print(ex)
            pass
if __name__=='__main__':
    urls = ['https://m.weibo.cn/api/statuses/repostTimeline?id=4380261561116383&page={}'.format(i) for i in range(4151,15000)]
    # with open('./data.csv', 'a+', encoding='utf_8_sig', newline='') as f:
    #     f_csv = csv.writer(f)
    #4151
    #     f_csv.writerow(['ok','msg','created_at','ids','mid','can_edit','raw_text','source','user_description',
    #           'user_follow_count','user_gender','user_id','user_mbrank','user_mbtype','user_profile_url',
    #           'user_profile_image_url','user_screen_name','user_statuses_count','user_urank,user_verified',
    #           'user_veridied_reason'])
    start(urls)