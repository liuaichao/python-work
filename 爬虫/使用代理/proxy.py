#使用代理服务器爬取淘宝
from urllib import request

url = "https://taobao.com"
proxy = {
    'http':"112.87.71.128:9999"
}
#创建proxyhandler
proxy_handler = request.ProxyHandler(proxy)
#创建opener
opener = request.build_opener(proxy_handler)
#安装opener
request.install_opener(opener)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
req = request.Request(url, headers=headers)
eq = request.urlopen(req)
res = eq.read().decode()
print(res)