#http://tieba.baidu.com/f?kw=%E6%9D%A8%E8%B6%85%E8%B6%8A&ie=utf-8&pn=50

from urllib import request,parse

base_url = "http://tieba.baidu.com/f?"
name = input("请输入吧名：")
page = input("请输入页数：")
re = {
    'kw':name,
    'pn':int(page)*50
}
url = base_url+parse.urlencode(re)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
}
req = request.Request(url, headers=headers)
op = request.urlopen(req)
res = op.read().decode()
print(res)