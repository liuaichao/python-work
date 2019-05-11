import requests
import json
headers = {

    'authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtYW4iOiJYaWFvbWkiLCJicmFuZCI6InhpYW9taSIsInN5c3RlbU5hbWUiOiJBbmRyb2lkIiwic3lzdGVtVmVyc2lvbiI6IjguMS4wIiwidW5pcXVlIjoiNzk5NDI1MTVlODZhOGIxNCIsInBsYXRmb3JtIjoiYW5kcm9pZCIsInVzZXJfY29kZSI6IkFERjhKSjVSSSIsInBrZ1B1c2hNYW5JZCI6Im1haW4iLCJwdXNoTWFuSWQiOiJtYWluIiwicmVnaXN0ZXJEYXRlIjoiMjAxOS0wMi0yNyIsImlhdCI6MTU1NTgzMzMwMiwiZXhwIjoxNTU1ODQ3NzAyfQ.ddiuo8FnosWnBQgz4iAvkz11Er0BEkXsaFNmZujBCh8',
    'content-type':	'application/json',
    'accept':'application/json',
    'callid':'eg6iWVAnv',
    'Host':	's.mfof.cn',
    'Accept-Encoding':'gzip',
    'User-Agent':'okhttp/3.12.1',
    'Connectiom':'keep-alive'
}

req = requests.get('http://s.mfof.cn/gw/res-bobo/bo/v1/api/app_resources?q=%7B%22%24and%22%3A%5B%7B%22group_'
                   'id%22%3A%22b8c1ae15c49eb44c25c36f2a30208568%22%7D%2C%7B%22group_id%22%3A%225b5d921b8d574ef5f8b3'
                   '97ed2c51b25b%22%7D%2C%7B%22group_id%22%3A%2271df259968cda98599fd5229d9deb145%22%7D%2C%7B%22group_i'
                   'd%22%3A%22f6da8301abac378a1b777183e544fede%22%7D%5D%7D&o=%5B%7B%22group_id%22%3A%227a61455a5cc3aab'
                   'f5dcd3c4b47b565b2%22%7D%5D&page=1&limit=10',headers=headers)
reqs = requests.get('http://s.mfof.cn/gw/res-bobo/bo/v1/api/app_resources/2a28e96f5828c6310d71a4e0c092c26a',headers=headers)

content = json.loads(req.text)['data']
print(type(content))
for i in content:
    content = i['title']
    path = i['cover_full']['01']['local']['path']
    id = i['id']
    print(id)
    print(content)
    print(path)
# print(reqs.text)
# with open('phtots.jpg','wb') as f:
#     f.write(reqs.content)
#https://images.bbvccz28.com/single/ju/images/5/a/1/9aeca49b9aed376f3b1094d7cd5052bb_full.jpg
#https://images.bbvccz28.com/single/njv/images/e/b/5/7872b370f1fcf96e69e211fad97eb9d4_thumbnails.jpg
#https://images.bbvccz28.com/single/hot/images/2/9/6/6afef214da4ae0aadb258253b6511_full.jpg
#https://images.bbvccz28.com/hls/a/e/d/2a28e96f5828c6310d71a4e0c092c26a.low.json/