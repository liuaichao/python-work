# -*- coding:utf-8 -*-
import requests
import json
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}
url = 'https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=%E5%8C%97%E4%BA%AC,0&kw=Java工程师&kt=3'
req = requests.get(url,headers=headers)
te = json.loads(req.text)
print(te['data']['results'])
