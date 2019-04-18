# -*- coding:utf-8 -*-
import requests,json
base_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%A3%81%E7%BA%B8&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%A3%81%E7%BA%B8&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=wallpaper&pn='
#https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%A3%81%E7%BA%B8&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%A3%81%E7%BA%B8&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=wallpaper&pn=90&rn=30&gsm=5a&1553474639583=
#https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%A3%81%E7%BA%B8&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%A3%81%E7%BA%B8&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=wallpaper&pn=60&rn=30&gsm=3c&1553474637361=
page = 30
file_url = r'D:\python程序\爬虫\异步请求-百度图片\img\\'
for i in range(1):
    url = base_url + str(page)
    req = requests.get(url)
    html = req.text.encode('utf-8')
    htmls = json.loads(html)
    # print(url)
    page = int(page)+30
    if page == 120:
        page = int(page)+30
    for j in range(29):
        img_url = htmls['data'][j]['thumbURL']
        img = requests.get(img_url)
        img_d = img.content
        # print(img_url)
        img_name = img_url.split('/')[-1].split(',')[-1].split('&')[0]
        print(img_name)
        with open(file_url+img_name+'.jpg', 'wb') as f:
            f.write(img_d)
