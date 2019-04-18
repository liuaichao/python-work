import requests
from lxml import etree
import re
def photo(base_url, headers):
    res = requests.get(base_url, headers)
    res = res.text
    url = re.findall('"objURL":"(.*?)",', res, re.S)
    print(url)
    name = 1
    for img in url:
        req = requests.get(img)
        with open(str(name)+".jpg", 'wb') as f:
             f.write(req.content)
        name = int(name)+1
    # html = etree.HTML(res.text)
    # img_src = html.xpath('//script[@type="text/javascript]"')
    # print(img_src)

if __name__=="__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11;Ubuntu; Linux x86_64; rv:58.0) Geck0/20100101 Firedox/58.0',
        'Referer': 'https://image.baidu.com/search/flip?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C0%CF%BB%A2&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
    }
    base_url = 'https://image.baidu.com/search/flip?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C0%CF%BB%A2&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
    photo(base_url, headers)

# res = requests.get('https://image.baidu.com/search/flip?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C0%CF%BB%A2&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111',headers=headers)
# with open("baidu.html", 'w', encoding='utf-8') as f:
#     f.write(res.text)