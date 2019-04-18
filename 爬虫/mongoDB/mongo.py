# -*- coding:utf-8 -*-
import pymongo

client = pymongo.MongoClient('192.168.0.200', 27017)
print(client)
db = client.test
post = {
    'name':'刘爱超',
    'sex':'男',
    'from':'济南'
}
posts = db.posts
posts_id = posts.insert_one(post).inserted_id
print(posts_id)