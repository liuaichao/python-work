'''
_json: true
callback: https://order.mi.com/login/callback?followup=https%3A%2F%2Fwww.mi.com%2Findex.html&sign=MjM0MWU0NjBlOTU1YzY4NGQzOTc3MDk4N2M2MjQ5Y2ZiZTMxNTFlZQ,,
sid: mi_eshop
qs:
_sign: 7X/6ZEYnMC4KAfOUCegeNWS3xLs=
serviceParam: {"checkSafePhone":false}
captCode: yqkdx
user: 17861404961
hash: 487F7EC7612093CDA56D324F712326E7
cc:

url:https://account.xiaomi.com/pass/serviceLoginAuth2?_dc=1552379776058
'''

from urllib import request,parse
from http import cookiejar
#创建cookiejar实例
cookie = cookiejar.CookieJar()
#生成cookie管理器
cookie_handle = request.HTTPCookieProcessor(cookie)
#创建http请求管理器
http_handle = request.HTTPHandler()
#生成https请求管理器
https_handle = request.HTTPSHandler()
#创建请求管理器
opener = request.build_opener(cookie_handle, http_handle, https_handle)

def login():
    url = 'https://account.xiaomi.com/pass/serviceLoginAuth2?_dc=1552379776058'
    data = {
        '_json': 'true',
        'callback': 'https://order.mi.com/login/callback?followup=https%3A%2F%2Fwww.mi.com%2Findex.html&sign=MjM0MWU0NjBlOTU1YzY4NGQzOTc3MDk4N2M2MjQ5Y2ZiZTMxNTFlZQ,,',
        'sid': 'mi_eshop',
        'qs':'lac981215lac',
        'sign': '7X/6ZEYnMC4KAfOUCegeNWS3xLs=',
        'serviceParam': '{"checkSafePhone":false}',
        'captCode': 'yqkdx',
        'user': '17861404961',
        'hash': '487F7EC7612093CDA56D324F712326E7',
        'cc':''
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
    data = parse.urlencode(data)
    req = request.Request(url, data=data.encode(),headers=headers)
    rsp = opener.open(req)
    print(rsp)
    url1 = 'https://i.mi.com/#/'
    rsp1 = opener.open(url1)
    html = rsp1.read().decode()
    with open(r'mi.html', 'a', encoding='utf-8') as f:
        f.write(html)


login()