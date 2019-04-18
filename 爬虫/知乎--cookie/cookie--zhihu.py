# -*- coding:utf-8 -*-
#https://www.zhihu.com/people/liu-ai-chao-6/activities
from urllib import request
if __name__ == '__main__':
    url = "https://www.zhihu.com/people/liu-ai-chao-6/activities"
    headers = {
        'Cookie':'tgw_l7_route=200d77f3369d188920b797ddf09ec8d1; _zap=b402748e-8948-40c5-98a3-4652f8c97573; _xsrf=AlbSJ6IBRVl59L1WatQhRS7IelNQPGVW; d_c0="AABigQaCsg6PTq11dhuKu4h-3vBAhKmHQO4=|1545277631"; capsion_ticket="2|1:0|10:1545277633|14:capsion_ticket|44:N2FmZWE0ZWJjYzg2NDM5NzhlZTBmZTBlYWFiZDJiYzQ=|f3f54318c533ff048e485b7a54af54adb1e45248c23d77b3047913608373e9ec"; z_c0="2|1:0|10:1545277645|4:z_c0|92:Mi4xUHp2ZEJ3QUFBQUFBSUNGdEJvS3lEaVlBQUFCZ0FsVk56VjRJWFFEYWkzQUxCVUphSmpxX2FqU3lWUjduOThCeGh3|77c9258835e395852515c32061eb7da7a8242e1843755e0ee005b7d310e405ba"; tst=r; q_c1=26a35be7e04741a99785882b4fb28e04|1545277647000|1545277647000'
    }
    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)