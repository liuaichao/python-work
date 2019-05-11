# -*- coding:utf-8 -*-
import requests
import json
headers = {

    'Host':	'cnd-01.ojdacloud.com:8090',
    'Accept-Encoding':'identity',
    'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi 5 Plus MIUI/V10.2.4.0.OEGCNXM)',
    'Connectiom':'keep-alive'
}
req = requests.get('http://cnd-01.ojdacloud.com:8090/media/km3u8/7bd/7bd2a9cc24ff4dd6abb2e2f96d3ff9f2/',headers=headers)
print(req.text)
#http://v.43lx74.cn/hls/d/6/3/42fd2c36cdde01cb9922237b2d9cf390.low.json/bbc-1-v1-a1.ts?sign=79cad4f977659b6d27196927a7a20cdd&t=1555833600
# http://v.43lx74.cn/hls/d/6/3/42fd2c36cdde01cb9922237b2d9cf390.low.json/bbc-2-v1-a1.ts?sign=d198589e9944e55156ba173f47427a80&t=1555833600
# http://v.43lx74.cn/hls/d/6/3/42fd2c36cdde01cb9922237b2d9cf390.low.json/bbc-3-v1-a1.ts?sign=4f67ab437fbfe270eb435c51165ccb2b&t=1555833600

