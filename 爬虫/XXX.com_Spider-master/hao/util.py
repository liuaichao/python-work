# -*- coding: utf-8 -*-

try:
    import zlib
    import sys
    import re
    import time ,pymysql,cgi,os,requests
    import datetime,random
    from xpinyin import Pinyin
    from hao.setting import *
except ImportError as e:
    print("模块导入 Error ==> util.py [{0}]".format(e))
    exit()

# 解码网站返回的压缩页面
def unzip_html(str):

    decompressed_data = zlib.decompress(str, 16 + zlib.MAX_WBITS)
    data_list = decompressed_data.decode('utf8').splitlines(True)
    html = ''

    for item in data_list:
        html += item

    return html

# 获取跳转后的地址
def location(url):
    try:
        try:
            result = requests.head(url=url,headers=user_agent)
            return result.headers['location']
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError,
                    requests.packages.urllib3.exceptions.ReadTimeoutError, requests.exceptions.ReadTimeout) as e:
            error("获取源码超时 Error ===> [ {0} ] 暂停后重启 {1}".format(url, e))
            time.sleep(10)
            location(url=url)
    except Exception as e:
        return e

# 获取编码
def get_encode():
    return sys.getfilesystemencoding()

# 获取时间戳
def getTime():
    return int(time.time())

# 汉字转拼音
def en(str):
    pinyin = Pinyin()
    result = re.findall(r'[\u4e00-\u9fa5]',string=str)
    string = ''
    for i in result:
        string += i
    result = pinyin.get_pinyin(string,u'')
    return result

# 转义html
def html(html):
    return pymysql.escape_string(cgi.escape(html))

# 反转义html
def unhtml(html):
    return html.replace('&amp;','&')

# 去除字符串空格
def strip(str):
    return str.strip()

# key
def ikey():
    d1 = datetime.datetime(2015, 1, 1)
    d2 = datetime.datetime.now()
    s = (d2 - d1).days * 24 * 60 * 60
    ms = d2.microsecond
    id1 = __has36(random.randint(36, 1295))
    id2 = __has36(s)
    id3 = __has36(ms + 46656)
    mId = id1 + id2 + id3
    return mId[::-1]
def __has36(num):
    key = 't5hrwop6ksq9mvfx8g3c4dzu01n72yeabijl'
    a = []
    while num != 0:
        a.append(key[num % 36])
        num = int(num / 36)
    a.reverse()
    out = ''.join(a)
    return out
# 异常处理
def error(err):
    log(err)
    if DEBUG:
        print(err)
    else:
        print(err)
        send(err)

# 日志
def log(info):
    logname = log_name
    if not os.path.exists(logname):
        os.mknod(logname)

    log_file = os.open(logname, os.O_APPEND | os.O_RDWR)
    info = "{0}   [ {1} ] \n".format(time.strftime("%F %H:%M:%S %p", time.localtime(getTime())), info)
    try:
        os.write(log_file, bytes(info, 'UTF-8'))
    except Exception as e:
        print("写入爬虫日志 Error ==> util.py  [{0}]".format(e))
    finally:
        os.close(log_file)

# 爬虫运行状况推送
def send(info):
    data = {
        'text': 'Running Log',
        'desp': '{0}  【 {1} 】'.format(info, time.strftime("%F %H:%M:%S %p", time.localtime(getTime())))
    }
    requests.post(server_put_url, data=data)

# 拼接sql语句
def get_sql(vinfo,v_type):
    if v_type == vod_type[0]:
        sql_str = 'INSERT INTO {0} (vkey,title,en_title,description,images,timelong,yuan_url,play_url,play_type,movie_type,inputtime) ' \
                  'VALUES ("{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}","{10}",{11});'.format(v_type,
            vinfo['vkey'],
            html(vinfo['title']),
            vinfo['en_title'],
            vinfo['description'],
            vinfo['images'],
            vinfo['vod_long'],
            vinfo['yuan_url'],
            vinfo['play_url'],
            vinfo['play_type'],
            vinfo['movie_type'],
            vinfo['inputtime'])

        return sql_str

    elif v_type == vod_type[1]:
        sql_str = 'INSERT INTO {0} (vkey,title,en_title,description,images,yuan_url,bt_url,movie_type,inputtime) ' \
                  'VALUES ("{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}",{9});'.format(v_type,
            vinfo['vkey'],
            html(vinfo['title']),
            vinfo['en_title'],
            vinfo['description'],
            vinfo['images'],
            vinfo['yuan_url'],
            vinfo['bt_url'],
            vinfo['movie_type'],
            vinfo['inputtime'])

        return sql_str

    else:
        error("无效的 <v_type> ")
        exit()
