#登录网址：https://www.huawei.com/en/accounts/LoginPost
'''
userName: 1395900558@qq.com
pwd: Rqe2PFiqE+HaW+QpuIlSVDZTtj5hvfDNR1LQvYQDIgIdlZW8p0jPhiOOvb0GZKODGQIfhjjZGqe+RKL4D1lEbxGn5F33E2w9hzhzI8ILnWf7vy3HoHiItz9yzlHUhSDrdtfWQIIzxahM6XhVVNbXYxx/3oaWWdBYT3HyGk/G9lo=
languages: zh
fromsite: www.huawei.com
authMethod: password
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
    url = 'https://www.huawei.com/en/accounts/LoginPost'
    data = {
        'userName': '1395900558@qq.com',
        'pwd': 'lac981215lac',
        'languages': 'zh',
        'fromsite': 'www.huawei.com',
        'authMethod': 'password'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
    }
    data = parse.urlencode(data)
    req = request.Request(url, data=data.encode(),headers=headers)
    rsp = opener.open(req)
    print(rsp)
    # url1 = 'https://www.huaweicloud.com/?utm_medium=menu&utm_source=corp_huawei&utm_campaign=allwayson'
    # rsp1 = opener.open(url1)
    # print(rsp1.read().decode())


login()