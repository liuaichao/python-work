# -*- coding:utf-8 -*-
from urllib import request,parse
from http import cookiejar
if __name__ == '__main__':

    #构建相关生成器
    cookie = cookiejar.CookieJar()
    cookie_handler = request.HTTPCookieProcessor(cookie)
    http_handler = request.HTTPHandler()
    https_handler = request.HTTPSHandler()
    opener = request.build_opener(http_handler, https_handler, cookie_handler)
    #定义函数进行登录
    def login():
        url = "http://www.renren.com/PLogin.do"
        data = {
            "email":"17861404961",
            "password":"lac981215lac"
        }
        data = parse.urlencode(data)
        req = request.Request(url, data=data.encode())
        #使用opener发起请求，用于获取cookie
        rsp = opener.open(req)
    #定义函数进行访问登陆后
    def getHomePage():
        url = "http://www.renren.com/969152844/profile"
        rsp = opener.open(url)
        html = rsp.read().decode('utf-8')
        print(type(html))
        with open(r'result.html','w',encoding='utf-8') as f:
            f.write(html)
        # print(html)
    #调用函数
    login()
    getHomePage()