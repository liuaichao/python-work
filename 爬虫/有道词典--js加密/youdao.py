'''
i: hello
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15524674544394
sign: d1b212c37011b2865ce6290121e3564e
ts: 1552467454439
bv: db6b9693e24ea152843dd96fcd289f0f
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
typoResult: false
'''
'''
salt:r = "" + (new Date).getTime()
          , i = r + parseInt(10 * Math.random(), 10)

'''
'''
sign:sign: n.md5("fanyideskweb" + e + i + "1L5ja}w$puC.v_Kz3@yYn")
'''

'''
Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 258
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: OUTFOX_SEARCH_USER_ID=1188532022@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=801780914.2595295; JSESSIONID=aaabaPrvQpPJL6TSgL2Lw; ___rl__test__cookies=1552472642259
Host: fanyi.youdao.com
Origin: http://fanyi.youdao.com
Referer: http://fanyi.youdao.com/
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36
X-Requested-With: XMLHttpRequest
'''
from urllib import request,parse,error
import time
import hashlib
import random
import json

def hx_sign(v):
    md5 = hashlib.md5()
    md5.update(bytes(v, encoding='utf-8'))
    sign = md5.hexdigest
    return sign
def fanyi(name):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    i = time.time()*1000 + random.randint(0,10)
    v = "fanyideskweb" + name + str(i) + "1L5ja}w$puC.v_Kz3@yYn"
    data = {
    'i': name,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': int(i),
    'sign': hx_sign(v),
    'ts': '1552467454439',
    'bv': 'db6b9693e24ea152843dd96fcd289f0f',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
    'typoResult': 'false'
    }
    data = parse.urlencode(data)
    headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Content-Length':len(data),
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'OUTFOX_SEARCH_USER_ID=1188532022@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=801780914.2595295; JSESSIONID=aaabaPrvQpPJL6TSgL2Lw; ___rl__test__cookies=1552480963274',
    'Host':'fanyi.youdao.com',
    'Origin':'http://fanyi.youdao.com',
    'Referer':'http://fanyi.youdao.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'

    }
    req = request.Request(url, data=data.encode(), headers=headers)
    res = request.urlopen(req)
    html = res.read().decode()
    data_json = json.loads(html)
    print(data_json['translateResult'][0][0]['tgt'])

if __name__ == '__main__':
    name = input('请输入要查找的单词：')
    try:
        fanyi(name)
    except error.HTTPError:
        print(1)
    except error.URLError:
        print(2)


